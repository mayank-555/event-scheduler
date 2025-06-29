from flask import Flask, request, jsonify
from utils import load_events, save_events
from notifier import send_email_notification
from datetime import datetime
from dateutil.relativedelta import relativedelta
import uuid
import threading
import time

app = Flask(__name__)


def sort_events(events):
    return sorted(events, key=lambda x: x['start_time'])



@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = {
        "id": str(uuid.uuid4()),
        "title": data.get("title"),
        "description": data.get("description"),
        "start_time": data.get("start_time"),
        "end_time": data.get("end_time"),
        "recurrence": data.get("recurrence", "none")
    }
    events = load_events()
    events.append(event)
    save_events(events)
    return jsonify({"message": "Event created", "event": event}), 201

@app.route('/events', methods=['GET'])
def list_events():
    events = sort_events(load_events())
    return jsonify(events), 200

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    events = load_events()
    for event in events:
        if event['id'] == event_id:
            event.update({
                "title": data.get("title", event["title"]),
                "description": data.get("description", event["description"]),
                "start_time": data.get("start_time", event["start_time"]),
                "end_time": data.get("end_time", event["end_time"]),
                "recurrence": data.get("recurrence", event["recurrence"]),
            })
            save_events(events)
            return jsonify({"message": "Event updated", "event": event}), 200
    return jsonify({"error": "Event not found"}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    events = load_events()
    new_events = [e for e in events if e['id'] != event_id]
    if len(new_events) == len(events):
        return jsonify({"error": "Event not found"}), 404
    save_events(new_events)
    return jsonify({"message": "Event deleted"}), 200

@app.route('/events/search', methods=['GET'])
def search_events():
    query = request.args.get('query', '').lower()
    events = load_events()
    matched = [e for e in events if query in e['title'].lower() or query in e['description'].lower()]
    return jsonify(matched), 200


sent_reminders = set()

def is_upcoming(event_time, now):
    return 0 <= (event_time - now).total_seconds() <= 3600  

def get_next_occurrence(event, now):
    recurrence = event.get("recurrence", "none").lower()
    start_time = datetime.fromisoformat(event["start_time"])

    while start_time < now:
        if recurrence == "daily":
            start_time += relativedelta(days=1)
        elif recurrence == "weekly":
            start_time += relativedelta(weeks=1)
        elif recurrence == "monthly":
            start_time += relativedelta(months=1)
        else:
            break
    return start_time

def check_reminders():
    while True:
        events = load_events()
        now = datetime.now()

        for event in events:
            try:
                recurrence = event.get("recurrence", "none").lower()

                
                next_time = (
                    get_next_occurrence(event, now)
                    if recurrence != "none"
                    else datetime.fromisoformat(event["start_time"])
                )

                event_id_key = f"{event['id']}:{next_time.isoformat()[:16]}"  

                if is_upcoming(next_time, now) and event_id_key not in sent_reminders:
                    subject = f"⏰ Reminder: {event['title']} at {next_time.strftime('%I:%M %p')}"
                    body = f"📝 Event: {event['title']}\n📅 Starts at: {next_time.strftime('%Y-%m-%d %H:%M')}\n📌 Description: {event['description'] or 'N/A'}"
                    send_email_notification(subject, body)
                    sent_reminders.add(event_id_key)

            except Exception as e:
                print(f"[Reminder Error] {e}")

        time.sleep(10)  


reminder_thread = threading.Thread(target=check_reminders, daemon=True)
reminder_thread.start()

if __name__ == '__main__':
    app.run(debug=True)

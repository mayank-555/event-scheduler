# app.py
from flask import Flask, request, jsonify
from utils import load_events, save_events
import uuid
from datetime import datetime

app = Flask(__name__)

# Helper: sort events by start time
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
    new_events = [event for event in events if event['id'] != event_id]
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

if __name__ == '__main__':
    app.run(debug=True)

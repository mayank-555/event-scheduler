# 🗓️ Event Scheduler System with Email Reminders

A Python Flask-based Event Scheduler backend that allows users to create, view, update, delete, and search events with persistent storage and automated **email reminders** (including recurring events).

---

## 🚀 Features

- ✅ Create, view, update, delete events
- 🔍 Search events by title/description
- 📁 Persistent JSON storage
- 🔁 Recurring events (daily, weekly, monthly)
- 📧 Email reminders sent 1 hour before event
- 🌐 Postman collection included for testing

---

## ⚙️ Tech Stack

- Python 3.x
- Flask
- `smtplib` + Gmail SMTP for email
- JSON (for persistence)
- Postman (for API testing)
- `python-dotenv` (for email config)

---

## 📦 Setup & Installation

### Step 1: Clone the repository

git clone https://github.com/mayank-555/event-scheduler.git
cd event-scheduler
###  Step 2: Create virtual environment

python3 -m venv venv


### Step 3: Activate virtual environment

source venv/bin/activate   # For Linux or MacOS
# OR
venv\Scripts\activate       # For Windows


### Step 4: Install dependencies

pip install -r requirements.txt
### Step 5: Configure environment

Create a .env file with:

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECEIVER=your_email@gmail.com
Step 6: Run the application

python app.py
App will start at: http://127.0.0.1:5000/

📮 API Endpoints
1. Create Event
POST /events

{
  "title": "Team Meeting",
  "description": "Discuss Q3 goals",
  "start_time": "2025-06-30T14:00:00",
  "end_time": "2025-06-30T15:00:00",
  "recurrence": "daily"   // Options: none, daily, weekly, monthly
}
2. View All Events
GET /events

3. Update Event
PUT /events/<event_id>

{
  "title": "Updated Title"
}
4. Delete Event
DELETE /events/<event_id>

5. Search Events
GET /events/search?query=meeting

🔔 Reminders & Notifications
Background thread checks events every minute

Email sent 1 hour before start time

Supports recurring events

🧪 Postman Instructions
Open Postman

Create a new Collection: Event Scheduler Collection

Save all requests (POST, GET, PUT, DELETE, SEARCH)

Export → Format: v2.1 → Save as postman_collection.json

### 🗂 Project Structure

```
.
├── .pytest_cache/             # pytest cache (ignore in Git)
├── __pycache__/               # Compiled Python cache
├── Output_Screenshots/        # Screenshots of Postman/API testing
├── tests/                     # Unit test files (e.g., test_event_scheduler.py)
├── venv/                      # Python virtual environment (ignore in Git)
├── .env                       # Gmail SMTP credentials (keep secret!)
├── app.py                     # Main Flask app with reminder thread
├── events.json                # Persistent event storage
├── notifier.py                # Email sending logic (Gmail SMTP)
├── postman_collection.json    # For testing API routes in Postman
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── test_event_scheduler.py    # Unit tests for scheduler functionality
├── utils.py                   # Load/save JSON event data
```



✅ Example Commands (cURL)
curl -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test",
    "description": "Test event",
    "start_time": "2025-07-01T10:00:00",
    "end_time": "2025-07-01T11:00:00"
  }'


View all event 

curl http://127.0.0.1:5000/events



📧 Author


Mayank Gupta


GitHub: @mayank-555


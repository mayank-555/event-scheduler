# 🗓️ Event Scheduler System

A simple Python Flask-based Event Scheduler backend that allows users to create, view, update, delete, and search events with persistent storage.

---

# 🚀 Features

- Create events
- View events (sorted by start time)
- Update existing events
- Delete events
- Search events by title/description
- Persistent JSON storage
- Postman collection included for testing

---

# ⚙️ Tech Stack

- Python 3.x
- Flask
- JSON (for persistence)
- Postman (for API testing)

---

# 📦 Setup & Installation

# Step 1: Clone the repository
git clone https://github.com/mayank-555/event-scheduler.git
cd event-scheduler

# Step 2: Create virtual environment
python3 -m venv venv

# Step 3: Activate virtual environment
source venv/bin/activate   # For Linux or MacOS
# OR
venv\Scripts\activate       # For Windows

# Step 4: Install dependencies
pip install Flask

# Step 5: Run the application
python app.py

# App will start at http://127.0.0.1:5000/

---

# 📮 API Endpoints

# 1. Create Event
POST /events
Body (JSON):
{
  "title": "Meeting",
  "description": "Project sync",
  "start_time": "2025-06-30T14:00:00",
  "end_time": "2025-06-30T15:00:00"
}

# 2. View All Events
GET /events

# 3. Update Event
PUT /events/<event_id>
Body (JSON):
{
  "title": "Updated Meeting Title"
}

# 4. Delete Event
DELETE /events/<event_id>

# 5. Search Event
GET /events/search?query=meeting

---

# 📤 Postman Instructions

# Step 1: Open Postman
# Step 2: Go to Collections → New Collection → Name it "Event Scheduler Collection"
# Step 3: Save all requests (POST, GET, PUT, DELETE, SEARCH) to the collection
# Step 4: Export the collection → Format: v2.1 → Save the .json file for submission

---

# 📁 Project Structure

.
├── app.py               # Main Flask application
├── utils.py             # Utility functions (load/save)
├── events.json          # Persistent event data
├── README.md            # This file
└── postman_collection.json  # Exported collection (submit this)

---

# ✅ Example Commands

# Add an event (cURL)
curl -X POST http://127.0.0.1:5000/events \
  -H "Content-Type: application/json" \
  -d '{"title":"Test","description":"Test event","start_time":"2025-07-01T10:00:00","end_time":"2025-07-01T11:00:00"}'

# View all events
curl http://127.0.0.1:5000/events

---

# 📧 Author

Mayank Gupta  

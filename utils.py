# utils.py
import json
import os

EVENTS_FILE = 'events.json'

def load_events():
    if not os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, 'w') as f:
            json.dump([], f)
    with open(EVENTS_FILE, 'r') as f:
        return json.load(f)

def save_events(events):
    with open(EVENTS_FILE, 'w') as f:
        json.dump(events, f, indent=4)

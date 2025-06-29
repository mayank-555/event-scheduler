import pytest
from app import app
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_event(client):
    event = {
        "title": "Test Event",
        "description": "Testing create endpoint",
        "start_time": "2025-07-29T02:43:00",
        "end_time": "2025-07-29T03:43:00",
        "recurrence": "none"
    }
    response = client.post('/events', json=event)
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Event created"
    assert data["event"]["title"] == event["title"]

def test_list_events(client):
    response = client.get('/events')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_search_event(client):
    response = client.get('/events/search?query=Test')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_update_event(client):
    # First, create an event to update
    new_event = {
        "title": "Update Test",
        "description": "Before update",
        "start_time": "2025-07-29T04:00:00",
        "end_time": "2025-07-29T05:00:00"
    }
    response = client.post('/events', json=new_event)
    event_id = response.get_json()["event"]["id"]

    # Now, update it
    updated_data = {"title": "Updated Title"}
    update_response = client.put(f'/events/{event_id}', json=updated_data)
    assert update_response.status_code == 200
    assert update_response.get_json()["event"]["title"] == "Updated Title"

def test_delete_event(client):
    # Create an event to delete
    event = {
        "title": "Delete Me",
        "description": "To be deleted",
        "start_time": "2025-07-29T06:00:00",
        "end_time": "2025-07-29T07:00:00"
    }
    response = client.post('/events', json=event)
    event_id = response.get_json()["event"]["id"]

    delete_response = client.delete(f'/events/{event_id}')
    assert delete_response.status_code == 200
    assert delete_response.get_json()["message"] == "Event deleted"

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_event(client):
    response = client.post('/events', json={
        "title": "Test",
        "description": "Pytest",
        "start_time": "2025-07-01T10:00:00",
        "end_time": "2025-07-01T11:00:00"
    })
    assert response.status_code == 201

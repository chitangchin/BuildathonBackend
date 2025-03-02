# tests/integration/test_location_endpoints.py
import pytest
from flask import jsonify

# Fake implementations for external services.
def fake_get_location_info(place, config, logger):
    return f"Fake description for {place}", None

def fake_text_to_speech(text, config, logger):
    # Return dummy audio bytes and no error.
    return b"dummy audio bytes", None

def test_get_location_info_no_param(client):
    # No place provided returns a 400 error.
    response = client.get('/get-location-info')
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data

def test_get_location_info_valid(client, monkeypatch):
    monkeypatch.setattr('routes.location_routes.get_location_info', fake_get_location_info)
    response = client.get('/get-location-info?place=Paris')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["place"] == "Paris"
    assert "Fake description" in json_data["description"]

def test_get_location_audio_no_param(client):
    response = client.get('/get-location-audio')
    assert response.status_code == 400
    json_data = response.get_json()
    assert "error" in json_data

def test_get_location_audio_valid(client, monkeypatch):
    monkeypatch.setattr('routes.location_routes.get_location_info', fake_get_location_info)
    monkeypatch.setattr('routes.location_routes.text_to_speech', fake_text_to_speech)
    response = client.get('/get-location-audio?place=Paris')
    # We expect a response with audio/mpeg mimetype and a Content-Disposition header.
    assert response.status_code == 200
    assert response.mimetype == 'audio/mpeg'
    assert 'attachment; filename=Paris.mp3' in response.headers.get('Content-Disposition')

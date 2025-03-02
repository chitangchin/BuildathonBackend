# tests/e2e/test_health.py
def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"

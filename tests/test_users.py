import pytest
from src.app import create_app

@pytest.fixture()
def client():
    app = create_app()
    return app.test_client()

def test_users_flow(client):
    r = client.get("/users")
    assert r.status_code == 200
    assert r.get_json() == []

    r = client.post("/users", json={"name": "Ana", "email": "ana@email.com"})
    assert r.status_code == 201
    new_id = r.get_json()["id"]

    r = client.get(f"/users/{new_id}")
    assert r.status_code == 200
    data = r.get_json()
    assert data["name"] == "Ana"
    assert data["email"] == "ana@email.com"

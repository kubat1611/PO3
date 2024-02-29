from src.api.app import app
import pytest


@pytest.fixture()
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_users_endpoint_returns_200(client):
    response = client.get("/users")
    assert response.status_code == 200


def test_create_and_get_user_endpoint_returns_200(client):
    response = client.post("/users", json={
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    user_id = response.json['id']
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200


def test_get_nonexistent_user_returns_404(client):
    response = client.get("/users/9999")
    assert response.status_code == 404


def test_create_user_with_valid_data_returns_201(client):
    response = client.post("/users", json={
        "first_name": "test",
        "last_name": "test",
        "birth_year": 2000,
        "group": "user"
    })
    assert response.status_code == 201


def test_create_user_with_invalid_data_returns_400(client):
    response = client.post("/users", json={
        "last_name": "test",
        "birth_year": "not_an_int",
        "group": "user"
    })
    assert response.status_code == 400


def test_update_user_with_valid_data_returns_200(client):
    response = client.patch("/users/1", json={"last_name": "updated"})
    assert response.status_code == 200


def test_delete_existing_user_returns_204(client):
    response = client.post("/users", json={
        "first_name": "Wojciech",
        "last_name": "Oczkowski",
        "birth_year": 1998,
        "group": "premium"
    })
    user_id = response.json['id']
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 204


def test_delete_nonexistent_user_returns_404(client):
    response = client.delete("/users/9999")
    assert response.status_code == 404

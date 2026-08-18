from fastapi.testclient import TestClient

from app.main import app
client = TestClient(app)


def test_register_user():
    response = client.post(
        "/auth/register",
        json={
            "full_name": "Test User",
            "email": "testuser@example.com",
            "password": "StrongPass123",
            "role": "employee"
        }
    )

    assert response.status_code in {201, 409}


def test_login_requires_form_data():
    response = client.post(
        "/auth/login",
        data={
            "username": "unknown@example.com",
            "password": "WrongPass123"
        }
    )

    assert response.status_code == 401


client = TestClient(app)


def test_register_user_duplicate():
    response = client.post(
        "/auth/register",
        json={
            "full_name": "Test User",
            "email": "testuser@example.com",
            "password": "StrongPass123",
            "role": "employee"
        }
    )

    assert response.status_code in {201, 409}


def test_login_successful():
    response = client.post(
        "/auth/login",
        data={
            "username": "unknown@example.com",
            "password": "WrongPass123"
        }
    )

    assert response.status_code == 401

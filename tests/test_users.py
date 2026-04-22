import pytest
from utils.json_validator import validate_json_schema

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"}
    },
    "required": ["id", "name", "username", "email"]
}

def test_get_users(api_client, logger):
    response = api_client.get("users")
    assert response.status_code == 200
    data = response.json()
    validate_json_schema(data[0], USER_SCHEMA)
    assert response.elapsed.total_seconds() < 2
    logger.info("GET /users passed")

def test_create_user(api_client, load_json_data, logger):
    users = load_json_data("data/users.json")
    for user in users:
        response = api_client.post("users", json=user)
        assert response.status_code == 201
        logger.info(f"Created user: {user['name']}")

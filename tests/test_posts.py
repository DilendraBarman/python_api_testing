import pytest
from utils.json_validator import validate_json_schema

POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"},
        "userId": {"type": "integer"}
    },
    "required": ["id", "title", "body", "userId"]
}

def test_get_posts(api_client, logger):
    response = api_client.get("posts")
    assert response.status_code == 200
    validate_json_schema(response.json()[0], POST_SCHEMA)
    assert response.elapsed.total_seconds() < 2
    logger.info("GET /posts passed")

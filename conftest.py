import pytest
import json
import logging
from utils.api_client import APIClient
import requests

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Environment to run tests: dev, staging, prod"
    )

@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env") or "dev"
    with open(f"config/{env}.json") as f:
        return json.load(f)

@pytest.fixture(scope="session")
def auth_token(config, logger=logging.getLogger("APITests")):
    auth_url = config.get("auth_url")
    payload = config.get("auth_payload")
    if not auth_url:
        logger.info("No auth_url provided, skipping token fetch")
        return None
    response = requests.post(auth_url, json=payload)
    assert response.status_code == 200, "Failed to fetch auth token"
    token = response.json().get("access_token")
    assert token, "Token not found in response"
    logger.info("Fetched auth token successfully")
    return token

@pytest.fixture(scope="session")
def api_client(config, auth_token=None):
    headers = config.get("default_headers", {})
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    return APIClient(
        base_url=config["base_url"],
        headers=headers,
        timeout=config.get("timeout"),
        max_retries=config.get("max_retries", 3),
        retry_delay=config.get("retry_delay", 1)
    )

@pytest.fixture(scope="session", autouse=True)
def logger():
    logging.basicConfig(filename="logs/api_test.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger("APITests")

@pytest.fixture
def load_json_data():
    import json
    def _loader(file_path):
        with open(file_path) as f:
            return json.load(f)
    return _loader

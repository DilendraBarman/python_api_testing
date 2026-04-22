import requests
import logging
from time import sleep

class APIClient:
    def __init__(self, base_url, headers=None, timeout=5, max_retries=3, retry_delay=1):
        self.base_url = base_url
        self.headers = headers or {}
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.logger = logging.getLogger("APIClient")

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        retries = 0
        while retries < self.max_retries:
            try:
                response = requests.request(method, url, headers=self.headers, timeout=self.timeout, **kwargs)
                self.logger.info(f"{method} {url} - Status: {response.status_code}")
                if response.status_code >= 500:
                    retries += 1
                    self.logger.warning(f"Retry {retries}/{self.max_retries} for {url}")
                    sleep(self.retry_delay)
                    continue
                return response
            except requests.RequestException as e:
                retries += 1
                self.logger.error(f"Request failed: {e}. Retry {retries}/{self.max_retries}")
                sleep(self.retry_delay)
        raise Exception(f"API request failed after {self.max_retries} retries: {url}")

    def get(self, endpoint, params=None):
        return self._request("GET", endpoint, params=params)

    def post(self, endpoint, json=None):
        return self._request("POST", endpoint, json=json)

    def put(self, endpoint, json=None):
        return self._request("PUT", endpoint, json=json)

    def delete(self, endpoint):
        return self._request("DELETE", endpoint)

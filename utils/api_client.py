import os
import requests
from dotenv import load_dotenv
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

load_dotenv()

class APIClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://jsonplaceholder.typicode.com")
        self.timeout = int(os.getenv("TIMEOUT", "10"))
        self.session = self._create_session()

    def _create_session(self):
        session = requests.session()
        session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

        retry=Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[500, 502, 503]
        )

        adapter = HTTPAdapter(max_retries=retry)
        session.mount("https://",adapter)

        return session
    
    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response
    
    def post(self, endpoint, params=None, json = None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, params=params, json=json, timeout=self.timeout)
        return response

    def put(self, endpoint, params=None, json = None):
        url= f"{self.base_url}{endpoint}"
        response = self.session.put(url, params=params, json=json, timeout=self.timeout)
        return response
    
    def patch(self, endpoint, params=None, json = None):
        url= f"{self.base_url}{endpoint}"
        response = self.session.patch(url, params=params, json=json, timeout=self.timeout)
        return response
    
    def delete(self, endpoint, params=None):
        url= f"{self.base_url}{endpoint}"
        response = self.session.delete(url, params=params, timeout=self.timeout)
        return response
    
    def close(self):
        self.session.close()

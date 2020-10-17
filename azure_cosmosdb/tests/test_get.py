import json
import pytest
import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def test_create():
    s = requests.Session()
    retries = Retry(total=10,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])
    s.mount('http://', HTTPAdapter(max_retries=retries))
    response = s.get("http://localhost:7071/api/Get")
    assert response.status_code == 404
import json
import requests
import pytest
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def test_create():
    s = requests.Session()
    retries = Retry(total=5,
                backoff_factor=0.1,
                status_forcelist=[ 500, 502, 503, 504 ])
    s.mount('http://', HTTPAdapter(max_retries=retries))
    payload = json.dumps({'text':"This is a sample texta"})
    response = s.post("http://localhost:8000/", data=payload)
    
    assert response.status_code == 200
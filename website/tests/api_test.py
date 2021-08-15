import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Keys
API_KEY = os.getenv('API_KEY')

def test_add_no_key():
    url = 'http://localhost:5000/addresses/parse/'


    mock_request_data = {
        'key': API_KEY + '--',
        'json-data': '[{ "name":"United Center", "address": "1901 W Madison St", "city": "Chicago", "state": "IL", "postal_code": "60612", "value": "medium" }, { "name":"Madison Square Garden", "address": "4 Pennsylvania Plaza", "city": "New York", "state": "NY", "postal_code": "10001", "value": "low" }]'
    }

    response = requests.post(url, data=mock_request_data)
    assert response.status_code == 403


def test_add_no_data():
    url = 'http://localhost:5000/addresses/parse/'

    mock_request_data = {
        'key': API_KEY,
        'json-data': ''
    }

    response = requests.post(url, data=mock_request_data)
    assert response.status_code == 400


def test_add_success():
    url = 'http://localhost:5000/addresses/parse/'

    mock_request_data = {
        'key': API_KEY,
        'json_data': '[{ "name":"United Center", "address": "1901 W Madison St", "city": "Chicago", "state": "IL", "postal_code": "60612", "value": "medium" }, { "name":"Madison Square Garden", "address": "4 Pennsylvania Plaza", "city": "New York", "state": "NY", "postal_code": "10001", "value": "low" }]'
    }

    response = requests.post(url, data=mock_request_data)
    assert response.status_code == 200
    assert response.json().get('success')
    assert response.json().get('success') == True


def test_get_no_key():
    url = 'http://localhost:5000/addresses/get/'

    response = requests.get(url)
    assert response.status_code == 403


def test_get_full():
    url = 'http://localhost:5000/addresses/get/'
    mock_request_params = {
        'key': API_KEY
    }

    response = requests.get(url, params=mock_request_params)
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0].get('address') != ''


def test_get_filter():
    url = 'http://localhost:5000/addresses/get/'
    mock_request_params = {
        'key': API_KEY,
        'value': 'high'
    }

    response = requests.get(url, params=mock_request_params)
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0].get('address')
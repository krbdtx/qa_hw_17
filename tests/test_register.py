import requests
from jsonschema import validate
from schemas.register import post_register_successful, post_register_unsuccessful
from .conftest import url_api


def test_post_register_successful(url_api):

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    response = requests.post(f"{url_api}/api/register", json=payload)
    body = response.json()
    validate(body, post_register_successful)

    assert response.status_code == 200
    assert body['id'] == 4
    assert body['token'] == "QpwL5tke4Pnpja7X4"


def test_post_register_unsuccessful(url_api):

    payload = {
        "email": "george.bluth@reqres.in",
        "password": ""
    }

    response = requests.post(f"{url_api}/api/register", json=payload)
    body = response.json()
    validate(body, post_register_unsuccessful)

    assert response.status_code == 400
    assert body['error'] == 'Missing password'

import requests
from jsonschema import validate
from schemas.user import get_list_users, get_single_user, post_create_user, put_update_user
from tests.conftest import URL


def test_get_list_users():

    per_page = 6
    response = requests.get(URL + '/api/users', params={"page": 2, "per_page": per_page})
    body = response.json()
    validate(body['data'], get_list_users)

    assert response.status_code == 200
    assert len(body['data']) <= per_page


def test_get_current_user():

    response = requests.get(URL + '/api/users/3')
    body = response.json()
    validate(body['data'], get_single_user)

    assert response.status_code == 200
    assert body['data']['id'] == 3
    assert body['data']['first_name'] == 'Emma'


def test_get_current_user_not_found():

    response = requests.get(URL + '/api/unknown/23')

    assert response.status_code == 404
    assert response.json() == {}


def test_post_create_user():

    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(URL + '/api/users', json=payload)
    body = response.json()
    validate(body, post_create_user)

    assert response.status_code == 201
    assert body['name'] == payload['name']
    assert body['job'] == payload['job']


def test_put_update_user():

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(URL + '/api/users/2', json=payload)
    body = response.json()
    validate(body, put_update_user)

    assert response.status_code == 200
    assert body['name'] == payload['name']
    assert body['job'] == payload['job']


def test_patch_update_user():

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(URL + '/api/users/2', json=payload)
    body = response.json()
    validate(body, put_update_user)

    assert response.status_code == 200
    assert body['name'] == payload['name']
    assert body['job'] == payload['job']


def test_delete_user():

    response = requests.delete(URL + '/api/users/2')

    assert response.status_code == 204

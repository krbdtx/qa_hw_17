import requests
from jsonschema import validate
from schemas.user import get_list_users, get_single_user, post_create_user, put_update_user
from tests.conftest import url_api


def test_get_list_users(url_api):

    per_page = 6
    response = requests.get(f'{url_api}/api/users', params={"page": 2, "per_page": per_page})
    body = response.json()
    validate(body['data'], get_list_users)

    assert response.status_code == 200
    assert len(body['data']) <= per_page


def test_get_current_user(url_api):

    response = requests.get(f'{url_api}/api/users/3')
    body = response.json()
    validate(body['data'], get_single_user)

    assert response.status_code == 200
    assert body['data']['id'] == 3
    assert body['data']['first_name'] == 'Emma'


def test_get_current_user_not_found(url_api):

    response = requests.get(f'{url_api}/api/unknown/23')

    assert response.status_code == 404
    assert response.json() == {}


def test_post_create_user(url_api):

    payload = {
        "name": "morpheus",
        "job": "leader"
    }

    response = requests.post(f'{url_api}/api/users', json=payload)
    body = response.json()
    validate(body, post_create_user)

    assert response.status_code == 201
    assert body['name'] == payload['name']
    assert body['job'] == payload['job']


def test_put_update_user(url_api):

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.put(f'{url_api}/api/users/2', json=payload)
    body = response.json()
    validate(body, put_update_user)

    assert response.status_code == 200
    assert body['name'] == payload['name']
    assert body['job'] == payload['job']


def test_patch_update_user(url_api):

    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    response = requests.patch(f'{url_api}/api/users/2', json=payload)
    body = response.json()
    validate(body, put_update_user)

    assert response.status_code == 200
    assert body['name'] == payload['name']
    assert body['job'] == payload['job']


def test_delete_user(url_api):

    response = requests.delete(f'{url_api}/api/users/2')

    assert response.status_code == 204

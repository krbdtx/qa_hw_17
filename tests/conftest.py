import pytest


@pytest.fixture(scope='module')
def url_api():
    return 'https://reqres.in'


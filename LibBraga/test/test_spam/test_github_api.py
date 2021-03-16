from unittest.mock import Mock

import pytest

from LibBraga import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/69489454?v=4'
    resp_mock.json.return_value = {
        'login': 'htjoao',
        'id': 69489454,
        'avatar_url': url,
    }
    get_mock = mocker.patch('LibBraga.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('htjoao')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('htjoao')
    assert 'https://avatars.githubusercontent.com/u/69489454?v=4' == url
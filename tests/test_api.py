import json
import pytest


@pytest.fixture
def app(mysql_service):
    from sample import app as sample_app
    yield sample_app


@pytest.fixture
def client(app, mysql_service):
    return app.test_client()


def test_get_users(app, client, mysql_service):
    res = client.get('/users/1')
    assert res.status_code == 200
    expected = {
        "id": 1,
        "name": "test_user1"
    }
    assert expected == json.loads(res.get_data(as_text=True))


def test_post_users(app, client, mysql_service):
    res = client.post(
        '/users',
        data=json.dumps(dict(email='email@mail.com', name='user')),
        content_type='application/json'
    )
    assert res.status_code == 201
    expected_user_name = "user"
    assert expected_user_name == json.loads(res.get_data(as_text=True))["name"]


def test_health(app, client, mysql_service):
    res = client.get('/health')
    assert res.status_code == 200
    expected = {
        "status": "healthy"
    }
    assert expected == json.loads(res.get_data(as_text=True))

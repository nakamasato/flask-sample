import json


def test_users(app, client):
    res = client.get('/users?user_id=1')
    assert res.status_code == 200
    expected = {
        "id": 1,
        "name": "test_user1"
    }
    assert expected == json.loads(res.get_data(as_text=True))


def test_health(app, client):
    res = client.get('/health')
    assert res.status_code == 200
    expected = {
        "status": "healthy"
    }
    assert expected == json.loads(res.get_data(as_text=True))

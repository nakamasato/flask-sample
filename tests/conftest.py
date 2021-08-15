import pytest

from sample import app as sample_app


@pytest.fixture
def app():
    yield sample_app


@pytest.fixture
def client(app):
    return app.test_client()

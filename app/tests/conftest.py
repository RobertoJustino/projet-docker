import pytest

from app import index


@pytest.fixture
def client():
    app = index()
    with app.test_client() as client:
        yield client
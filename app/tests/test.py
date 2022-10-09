from pickle import TRUE
import pytest
from app import app
import mysql.connector



@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get('/')
    assert resp.status_code == 200

def test_api_mangas(client):
    resp = client.get('/api/mangas')
    assert resp.status_code == 200

def test_api_mangas_id(client):
    resp = client.get('/api/mangas/1')
    assert resp.status_code == 200

def test_api_mangas_id_genres(client):
    resp = client.get('/api/mangas/1/genres')
    assert resp.status_code == 200

def test_api_mangas_id_reviews(client):
    resp = client.get('/api/mangas/1/reviews')
    assert resp.status_code == 200

def test_db(client):
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'goodreads'
    }
    connection = mysql.connector.connect(**config)
    assert connection.is_connected()
    connection.close()


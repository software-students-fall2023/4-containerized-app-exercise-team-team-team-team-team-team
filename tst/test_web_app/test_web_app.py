"""Does tests for ze program"""
import os
import pytest
import json
import base64
from dotenv import load_dotenv
from src.machine_learning_client.main import detect_encoding, connect_to_db 

load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_dashboard_route(client):
    """Test the dashboard route."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"homepage.html" in response.data  

def test_data_collection_get_route(client):
    """Test the data collection GET route."""
    response = client.get("/data_collection")
    assert response.status_code == 200
    assert b"data_collection.html" in response.data

def test_data_collection_post_route(client):
    """Test the data collection POST route."""
    image_data = base64.b64encode(b'Test Image Data').decode('utf-8')
    response = client.post("/data_collection", json={'image': f'data:image/png;base64,{image_data}'})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert 'Image uploaded successfully' in data['message']

def test_connection_to_db_successful(db_connection_string):
    """Tests connection to DB"""
    ml_data, db = connect_to_db(db_connection_string)
    assert ml_data is not None
    assert db is not None

def test_collection_and_database_exist(db_connection_string):
    """Tests db connection and existence"""
    ml_data, db = connect_to_db(db_connection_string)
    assert ml_data.name == "DataForMachineLearning"
    assert db.name == "MLData"

def test_detect_encoding1():
    """Tests detect encoding 1"""
    file_path = "tests/testFile1.txt"
    detect_encoding(file_path)


def test_detect_encoding2():
    """Tests detect encoding 2"""
    detect_encoding("test/testFile1.txt")


def test_detect_encoding3():
    """Tests detect encoding 3"""
    file_path = "tests/testFile1.txt"
    detect_encoding(file_path)
    detect_encoding("test/testFile2.txt")

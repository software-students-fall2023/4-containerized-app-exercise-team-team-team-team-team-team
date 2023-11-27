"""Does tests for ze program"""
import os
import pytest
from dotenv import load_dotenv
from src.web_app.web_app import connect_to_db
from src.machine_learning_client.main import detect_encoding

load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')

@pytest.fixture
def database_connection_string():
    """DB connection string"""
    return DATABASE_CONNECTION_STRING
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
    file_path = 'tests/testFile1.txt'
    detect_encoding(file_path)

def test_detect_encoding2():
    """Tests detect encoding 2"""
    detect_encoding('test/testFile1.txt')

def test_detect_encoding3():
    """Tests detect encoding 3"""
    file_path = 'tests/testFile1.txt'
    detect_encoding(file_path)
    detect_encoding('test/testFile2.txt')

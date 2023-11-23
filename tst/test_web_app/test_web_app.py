"""Test Everything!"""
import pymongo
import pymongo.errors
import pytest
import os
from dotenv import load_dotenv
from src.web_app.web_app import connectToDB
from src.machine_learning_client.main import detect_encoding
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')

@pytest.fixture
def database_connection_string():
    """gets db connection string"""
    return DATABASE_CONNECTION_STRING
def test_connection_to_db_successful(database_connection_string):
    """Test Number 1 for checking db connection"""
    ml_data, db = connectToDB(database_connection_string)
    assert ml_data is not None 
    assert db is not None

def test_collection_and_database_exist(database_connection_string):
    """Test Number 1 for checking db"""
    ml_data, db = connectToDB(database_connection_string)
    assert ml_data.name == "DataForMachineLearning"
    assert db.name == "MLData"

def test_detect_encoding1():
    """Test Number 1 for checking encoding"""
    file_path = 'tests/testFile1.txt'
    detect_encoding(file_path) 

def test_detect_encoding2():
    """Test Number 2 for checking encoding"""
    detect_encoding('test/testFile1.txt')

def test_detect_encoding3():
    """Test Number 3 for checking encoding"""
    file_path = 'tests/testFile1.txt'
    detect_encoding(file_path)
    detect_encoding('test/testFile2.txt')

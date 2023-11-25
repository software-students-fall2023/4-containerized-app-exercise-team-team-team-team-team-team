import pymongo
import pymongo.errors
import pytest
import os
from dotenv import load_dotenv
from src.web_app.web_app import connectToDB
from machine_learning_client.main import *

load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')

@pytest.fixture
def database_connection_string():
    return DATABASE_CONNECTION_STRING
def test_connection_to_db_successful(database_connection_string):
    ml_data, db = connectToDB(database_connection_string)
    assert ml_data is not None 
    assert db is not None

def test_collection_and_database_exist(database_connection_string):
    ml_data, db = connectToDB(database_connection_string)
    assert ml_data.name == "DataForMachineLearning"
    assert db.name == "MLData"

def TEST_detect_encoding1():
    FILE_PATH = 'tests/testFile1.txt'
    detect_encoding(FILE_PATH)
    

def TEST_detect_encoding2():
    detect_encoding('test/testFile1.txt')

def TEST_detect_encoding2():
    FILE_PATH = 'tests/testFile1.txt'
    detect_encoding(FILE_PATH)
    detect_encoding('test/testFile2.txt')


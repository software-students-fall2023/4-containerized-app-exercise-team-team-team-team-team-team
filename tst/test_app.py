"""Modules"""
import os
import pymongo
import pytest
from dotenv import load_dotenv
from src.web_app.web_app import connect_to_db
from src.machine_learning_client.main import main


load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")


@pytest.fixture
def database_connection_string():
    """Creating standard database connection string load."""
    return DATABASE_CONNECTION_STRING


def test_connection_to_db_successful():
    """Testing that connection values found are non null."""
    ml_data, db = connect_to_db(DATABASE_CONNECTION_STRING)
    assert ml_data is not None
    assert db is not None


def test_collection_and_database_exist():
    """Finding"""
    ml_data, db = connect_to_db(DATABASE_CONNECTION_STRING)
    assert ml_data.name == "DataForMachineLearning"
    assert db.name == "MLData"

def test_main():
    main()
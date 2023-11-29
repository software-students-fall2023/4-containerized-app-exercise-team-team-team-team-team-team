"""Does tests for ze program"""
import os

# import json
# import base64
from dotenv import load_dotenv
from src.web_app import connect_to_db
from src.main import detect_encoding


load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")


def database_connection_string():
    """DB connection string"""
    return DATABASE_CONNECTION_STRING


def test_connection_to_db_successful():
    """Tests connection to DB"""
    ml_data, database = connect_to_db(database_connection_string())
    assert ml_data is not None
    assert database is not None


def test_collection_and_database_exist():
    """Tests db connection and existence"""
    ml_data, database = connect_to_db(database_connection_string())
    assert ml_data.name == "DataForMachineLearning"
    assert database.name == "MLData"


def test_detect_encoding1():
    """Tests detect encoding 1"""
    file_path = "tst/test_web_app/tests/testFile1.txt"
    detect_encoding(file_path)


def test_detect_encoding2():
    """Tests detect encoding 2"""
    detect_encoding("tst/test_web_app/tests/testFile1.txt")


def test_detect_encoding3():
    """Tests detect encoding 3"""
    file_path = "tst/test_web_app/tests/testFile1.txt"
    detect_encoding(file_path)
    detect_encoding("tst/test_web_app/tests/testFile1.txt")


# @pytest.fixture
# def client():
#     app.config["TESTING"] = True
#     with app.test_client() as client:
#         yield client


# def test_data_collection_get_route(client):
#     """Test the data collection GET route."""
#     response = client.get("/data_collection")
#     assert response.status_code == 200
#     assert b"data_collection.html" in response.data


# def test_data_collection_post_route(client):
#     """Test the data collection POST route."""
#     image_data = base64.b64encode(b"Test Image Data").decode("utf-8")
#     response = client.post(
#         "/data_collection", json={"image": f"data:image/png;base64,{image_data}"}
#     )
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert "Image uploaded successfully" in data["message"]


# def test_data_collection_post_route(client):
#     """Test the data collection POST route."""
#     image_data = base64.b64encode(b"Test Image Data").decode("utf-8")
#     response = client.post(
#         "/data_collection", json={"image": f"data:image/png;base64,{image_data}"}
#     )
#     assert response.status_code == 200
#     data = json.loads(response.data)
#     assert "Image uploaded successfully" in data["message"]

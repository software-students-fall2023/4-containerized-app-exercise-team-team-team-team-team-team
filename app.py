"""
Modules
"""
import os
import logging
import pymongo
import flask
from dotenv import load_dotenv

app = flask.Flask(__name__)
logging.basicConfig(level=logging.INFO)
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
log = logging.getLogger()

@app.route('/')
def main_page():
    """Main page renders the index.html page"""
    return flask.render_template('index.html')
def connect_to_db(connection_string):
    """This function connects to the database"""
    try:
        client = pymongo.MongoClient(connection_string)
        db = client.MLData
        ml_data = db.get_collection('DataForMachineLearning')
        return ml_data, db
    except Exception as e:
        print(f"Exception type:{type(e)}")
        raise
log = logging.getLogger()
collection, data_base = connect_to_db(DATABASE_CONNECTION_STRING)

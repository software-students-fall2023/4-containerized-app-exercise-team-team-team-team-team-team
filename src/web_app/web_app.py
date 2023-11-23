"""Web App Stuff!"""
import logging
import os
from dotenv import load_dotenv
import pymongo



logging.basicConfig(level=logging.INFO)
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
print("hello world")
log = logging.getLogger()

def connectToDB(connectionString):
    """Connects to MongoDB database"""
    try:
        client = pymongo.MongoClient(connectionString)
        db = client.MLData
        mlData = db.get_collection('DataForMachineLearning')
        print("que")
        return mlData, db
    except Exception as e:
        print(f"Exception type: {type(e)}")
        # log.error(f"Unsuccessful login to client. Error code:{e}")
        print("made it here")
        raise


log = logging.getLogger()
collection, dataBase = connectToDB(DATABASE_CONNECTION_STRING)

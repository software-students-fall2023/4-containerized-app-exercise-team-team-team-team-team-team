"""Holds all of the informationn for the web app"""
import base64
import os
import logging
import pymongo
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
logging.basicConfig(level=logging.INFO)
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
log = logging.getLogger()
app = Flask(__name__)

def connect_to_db(connection_string):
    """Connects to DB"""
    try:
        client = pymongo.MongoClient(connection_string)
        db = client.MLData
        ml_data = db.get_collection('DataForMachineLearning')
        # print("que")
        return ml_data, db
    except ConnectionError as e:
        logging.error("Exception connecting to MongoDB: %s",e)
        raise
        # print(f"Exception type: {type(e)}")
        # # log.error(f"Unsuccessful login to client. Error code:{e}")
        # print("made it here")
        # raise


log = logging.getLogger()
collection, dataBase = connect_to_db(DATABASE_CONNECTION_STRING)

@app.route('/')
def view_dashboard():
    """renders dashboard"""
    return render_template('homepage.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    """Uploads image"""
    try:
        image_data = request.json['image']
        # extracting base64 image data
        image_binary = base64.b64decode(image_data.split(',')[1])
        # if size is an issue we can convert it from base64 to binary
        # storing in mongodb
        result = collection.insert_one({"image": image_binary})
        return jsonify({"message": "Image uploaded successfully", "id": str(result.inserted_id)})
        # inserted_id contains unique ID assigned by MongoDB to image
    except ConnectionError as e:
        logging.error("Error uploading image: %s",e)
        return jsonify({"error": "Error uploading image"}), 500

if __name__ == '__main__':
    app.run(debug=True)

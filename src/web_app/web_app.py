from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
import pymongo
import os
import logging
import base64 

logging.basicConfig(level=logging.INFO)
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
#print("hello world")
log = logging.getLogger()
app = Flask(__name__)

def connectToDB(connectionString):
    try:
        client = pymongo.MongoClient(connectionString)
        db = client.MLData
        mlData = db.get_collection('DataForMachineLearning')
        # print("que")
        return mlData, db
    except Exception as e:
        logging.error(f"Exception connecting to MongoDB: {e}")
        raise
        # print(f"Exception type: {type(e)}")
        # # log.error(f"Unsuccessful login to client. Error code:{e}")
        # print("made it here")
        # raise


log = logging.getLogger()
collection, dataBase = connectToDB(DATABASE_CONNECTION_STRING)

@app.route("/")
def view_dashboard():
    """renders dashboard"""
    return render_template("homepage.html")


@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        image_data = request.json['image'] # extracting base64 image data
        image_binary = base64.b64decode(image_data.split(',')[1]) # if size is an issue we can convert it from base64 to binary 

        # storing in mongodb
        result = collection.insert_one({"image": image_binary})
        return jsonify({"message": "Image uploaded successfully", "id": str(result.inserted_id)}) # inserted_id contains unique ID assigned by MongoDB to image
    except Exception as e:
        logging.error(f"Error uploading image: {e}")
        return jsonify({"error": "Error uploading image"}), 500

if __name__ == '__main__':
    app.run(debug=True)

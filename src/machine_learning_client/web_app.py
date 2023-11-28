"""All necessary imports to run web_app.py"""
import os
import asyncio
import logging
import base64
import time
import pymongo
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from main import main, detect_encoding

# import pymongo


logging.basicConfig(level=logging.INFO)
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
log = logging.getLogger()
app = Flask(__name__)

def connect_to_db(connectionString):
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
collection, dataBase = connect_to_db(DATABASE_CONNECTION_STRING)


@app.route("/")
def view_dashboard():
    """renders dashboard"""
    return render_template("homepage.html")


@app.route("/data_collection", methods=["GET"])
def data_collection_get():
    """gets page for data collection"""
    return render_template("data_collection.html")


@app.route("/data_collection", methods=["POST"])
def data_collection_post():
    """handles post request of photo that was collected on page"""
    try:
        image_data = request.json["image"]  # extracting base64 image data
        image_binary = base64.b64decode(image_data.split(",")[1])  # decode the image

        # determining file path
        script_dir = os.path.dirname(__file__)  # directory of the script
        target_dir = os.path.join(
            script_dir, "..", "..", "images"
        )  # navigating up 'images' folder
        # os.makedirs(target_dir, exist_ok=True)
        # -> creating directory if it doesn't exist, might be an issue on other machines

        # defining file name, it doesn't need to be unique if docker file clears image folder
        file_path = os.path.join(target_dir, "uploaded_image.png")

        # writing image data into a file
        with open(file_path, "wb") as file:
            file.write(image_binary)
        
        stuff=asyncio.run(main())
        writeOut(stuff)
        return jsonify(
            {"message": "Image uploaded successfully", "file_path": file_path}
        )

    except Exception as e:
        logging.error("Error uploading image: %s", e)
        return jsonify({"error": "Error uploading image"}), 500


def writeOut(stuff):
    fp_out = "output.txt"
    encoding = detect_encoding(fp_out)
    with open(fp_out, 'w',encoding=encoding) as outp:
        outp.write(stuff[0]+","+str(stuff[1]))


if __name__ == "__main__":
    app.run(debug=True)
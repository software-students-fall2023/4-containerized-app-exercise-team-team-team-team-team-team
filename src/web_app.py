"""All necessary imports to run web_app.py"""
import os
import asyncio
import logging
import base64
import pymongo
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from main import main


logging.basicConfig(level=logging.INFO)
load_dotenv()
DATABASE_CONNECTION_STRING = os.getenv("DATABASE_CONNECTION_STRING")
log = logging.getLogger()
app = Flask(__name__)
app.secret_key = "no body no crime"


def connect_to_db(connection_string):
    """Connects to DB"""
    try:
        client = pymongo.MongoClient(connection_string)
        database = client.MLData
        ml_data = database.get_collection("DataForMachineLearning")
        return ml_data
    except ConnectionError as error:
        logging.error("Exception connecting to MongoDB: %s", error)
        raise
        # print(f"Exception type: {type(e)}")
        # # log.error(f"Unsuccessful login to client. Error code:{e}")
        # print("made it here")
        # raise


log = logging.getLogger()
ml_collection = connect_to_db(DATABASE_CONNECTION_STRING)


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
            script_dir, "..", "images"
        )  # navigating up 'images' folder
        # os.makedirs(target_dir, exist_ok=True)
        # -> creating directory if it doesn't exist, might be an issue on other machines

        # defining file name, it doesn't need to be unique if docker file clears image folder
        file_path = os.path.join(target_dir, "uploaded_image.png")

        # writing image data into a file
        with open(file_path, "wb") as file:
            file.write(image_binary)
        # return redirect(url_for('return_emotion'))

        return jsonify(
            {"message": "Image uploaded successfully", "file_path": file_path}
        )

    except ConnectionError as error:
        logging.error("Error uploading image: %s", error)
        return jsonify({"error": "Error uploading image"}), 500


@app.route("/data_output", methods=["GET"])
def return_emotion():
    """returns emotion to the output page"""

    # Run the main coroutine concurrently
    result = asyncio.run(main())

    emotion = result[0]
    emotion_dic = {"emotion": emotion}
    ml_lib = connect_to_db(DATABASE_CONNECTION_STRING)
    ml_lib.insert_one(emotion_dic)
    # collect data from ml_lib
    db_emotion_list = {}
    for doc in ml_lib.find():
        emote = doc.get("emotion")
        if emote in db_emotion_list:
            db_emotion_list[emote] += 1
        else:
            db_emotion_list[emote] = 1
    # with open("output.txt", "w", encoding="utf-8") as output_file:
    #     for key, value in db_emotion_list.items():
    #         if key is not None:
    #             output_file.write(f"{key},{value}\n")

    # output_file.close()

    return render_template(
        "data_output.html", emotion=emotion, emotions_data=db_emotion_list
    )


if __name__ == "__main__":
    app.run(debug=True)

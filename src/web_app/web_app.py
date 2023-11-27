# from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
# import pymongo
import os
import logging
import base64 

logging.basicConfig(level=logging.INFO)
# load_dotenv()
# DATABASE_CONNECTION_STRING = os.getenv('DATABASE_CONNECTION_STRING')
#print("hello world")
log = logging.getLogger()
app = Flask(__name__)

# def connectToDB(connectionString):
#     try:
#         client = pymongo.MongoClient(connectionString)
#         db = client.MLData
#         mlData = db.get_collection('DataForMachineLearning')
#         # print("que")
#         return mlData, db
#     except Exception as e:
#         logging.error(f"Exception connecting to MongoDB: {e}")
#         raise
#         # print(f"Exception type: {type(e)}")
#         # # log.error(f"Unsuccessful login to client. Error code:{e}")
#         # print("made it here")
#         # raise


log = logging.getLogger()
# collection, dataBase = connectToDB(DATABASE_CONNECTION_STRING)

@app.route('/')
def view_dashboard():
    return render_template('homepage.html')

@app.route('/data_collection', methods=['GET'])
def data_collection_get():
    return render_template('data_collection.html')

@app.route('/data_collection', methods=['POST'])
def data_collection_post():
    try:
        image_data = request.json['image']  # extracting base64 image data
        image_binary = base64.b64decode(image_data.split(',')[1])  # decode the image

        # determining file path
        script_dir = os.path.dirname(__file__)  # directory of the script
        target_dir = os.path.join(script_dir, '..', '..', 'images')  # navigating up 'images' folder
        # os.makedirs(target_dir, exist_ok=True)  -> creating  directory if it doesn't exist, not sure if this might be an issue on other machines...

        # defining file name, it doesn't need to be unique if docker file clears image folder
        file_path = os.path.join(target_dir, 'uploaded_image.png') 

        # writing image data into a file
        with open(file_path, 'wb') as file:
            file.write(image_binary)

        return jsonify({"message": "Image uploaded successfully", "file_path": file_path})

    except Exception as e:
        logging.error(f"Error uploading image: {e}")
        return jsonify({"error": "Error uploading image"}), 500


if __name__ == '__main__':
    app.run(debug=True)



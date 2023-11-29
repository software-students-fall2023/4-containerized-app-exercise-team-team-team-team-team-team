"""Accesses the Hume Machine Learning API client and pulls the emotion from the image"""
import json
import os
import chardet
from dotenv import load_dotenv
from hume import HumeStreamClient
from hume.models.config import FaceConfig


def get_image():
    """Grabs the only image in the images folder!"""
    script_direct = os.path.dirname(os.path.abspath(__file__))
    images_path = os.path.join(script_direct, "..", "images")
    return os.path.join(images_path, os.listdir(images_path)[0])


def detect_encoding(file_path):
    """Figures out encoding"""
    with open(file_path, "rb") as f1:
        result = chardet.detect(f1.read())
    return result["encoding"]


script_dir = os.path.dirname(os.path.abspath(__file__))
FILE_PATH_API = os.path.join(script_dir, "config.json")
FILE_PATH_IMAGE = get_image()
encodingAPI = detect_encoding(FILE_PATH_API)
encodingImage = detect_encoding(FILE_PATH_IMAGE)


with open(FILE_PATH_API, "r", encoding=encodingAPI) as f:
    configs = json.load(f)
#! Figure out how to containerize this.
API_TOKEN = configs["api_token"]


async def main():
    """Hume API CopyPasta"""
    load_dotenv()
    client = HumeStreamClient(API_TOKEN)
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file(FILE_PATH_IMAGE)
        emotions = (result.get("face").get("predictions")[0]).get("emotions")
        max_num = 0
        max_emotion = ""
        for i in emotions:
            if i.get("score") > max_num:
                max_num = i.get("score")
                max_emotion = i.get("name")
        max_emotion = max_emotion + ""
        return [max_emotion, max_num]
"""Accesses the Hume Machine Learning API client and pulls the emotion from the image"""
import json
import os
import chardet
from hume import HumeStreamClient
from hume.models.config import FaceConfig


def get_image():
    """Grabs the only image in the images folder!"""
    files = os.listdir("images")
    return "images/" + files[0]


def detect_encoding(file_path):
    """Figures out encoding"""
    with open(file_path, "rb") as f1:
        result = chardet.detect(f1.read())
    return result["encoding"]


FILE_PATH_API = "src/machine_learning_client/config.json"
FILE_PATH_IMAGE = get_image()
encodingAPI = detect_encoding(FILE_PATH_API)
encodingImage = detect_encoding(FILE_PATH_IMAGE)


with open(FILE_PATH_API, "r", encoding=encodingAPI) as f:
    configs = json.load(f)

API_TOKEN = configs["api_token"]


async def main():
    """Hume API CopyPasta"""
    client = HumeStreamClient(API_TOKEN)
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file(FILE_PATH_IMAGE)
        emotions = (result.get("face").get("predictions")[0]).get("emotions")
        max_num = 0
        max_emotion = "abc"
        for i in emotions:
            if i.get("score") > max_num:
                max_num = i.get("score")
                max_emotion = i.get("name")
        max_emotion = max_emotion + ""
        return [max_emotion, max_num]

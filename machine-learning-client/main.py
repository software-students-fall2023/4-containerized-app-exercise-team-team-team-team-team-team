import json
import requests
import asyncio
import os,sys
from hume import HumeStreamClient, StreamSocket
from hume.models.config import FaceConfig


with open('machine-learning-client/config.json', 'r') as f:
    config = json.load(f)

API_TOKEN = config['api_token']


async def main():
    client = HumeStreamClient(API_TOKEN)
    config = FaceConfig(identify_faces=True)
    async with client.connect([config]) as socket:
        result = await socket.send_file("images/imagetest1.png")
        fle = open('output.txt','w')
        sys.stdout = fle
        print(result)

asyncio.run(main())
from turtle import st
from numpy import positive
import requests
import json
import gettext

import io
import base64
from PIL import Image

CLIENT_KEY = '55f22dc5ceaa6f6b57a9081106ce43c7aef5707d1812fac6ac4cb9c425cf843a'
URL = 'https://api-us.restb.ai/vision/v2/multipredict'

class ScoreImage:
    def _init_(self) -> None:
        self.kitchen = None
        self.bathroom = None
        self.bedroom = None
        self.frontal = None

    def getScore(imageBase64):

        payload = {
            # Add your client key
            'client_key': CLIENT_KEY,
            'model_id': 're_condition',
            # Add the image URL you want to process
            'image_base64': imageBase64
        }

        response = requests.get(URL, params=payload)

        # The response is formatted in JSON
        json_response = response.json()
        # print(json_response)
        return json_response["response"]["solutions"]["re_condition"]["score"]

    def getScoreImages(self, kitchen_url, bathroom_url, bedroom_url, frontal_url):
        print("getScoreImages")
        result = []
        # print(newImage)
        a = ScoreImage.getScore(kitchen_url)
        print("getScore",a)
        result.append(a)
        result.append(ScoreImage.getScore(bathroom_url))
        result.append(ScoreImage.getScore(bedroom_url))
        result.append(ScoreImage.getScore(frontal_url))
        print("Ahi va el result", result)
        return result
        

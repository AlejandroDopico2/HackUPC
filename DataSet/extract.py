CLIENT_KEY = "55f22dc5ceaa6f6b57a9081106ce43c7aef5707d1812fac6ac4cb9c425cf843a"
import json
from time import sleep
import requests

import numpy as np

url = 'https://api-us.restb.ai/vision/v2/multipredict'

def getScore(imageUrl):

    payload = {
        # Add your client key
        'client_key': CLIENT_KEY,
        'model_id': 're_features_v3',
        # Add the image URL you want to process
        'image_url': imageUrl
    }

    response = requests.get(url, params=payload)

    # The response is formatted in JSON
    json_response = response.json()
    # print(json_response)
    return json_response["response"]["solutions"]["re_condition"]["score"]

output = open("features.txt", 'a')
for i in range(1, 536):
    image_url = "https://raw.githubusercontent.com/emanhamed/Houses-dataset/master/Houses%20Dataset/" + str(i) + "_bathroom.jpg"
    output.write(str(getScore(image_url)) + "\t")
    # sleep(0.5)
    image_url = "https://raw.githubusercontent.com/emanhamed/Houses-dataset/master/Houses%20Dataset/" + str(i) +"_bedroom.jpg"
    output.write(str(getScore(image_url)) + "\t")
    # sleep(0.5)
    image_url = "https://raw.githubusercontent.com/emanhamed/Houses-dataset/master/Houses%20Dataset/" + str(i) +"_kitchen.jpg"
    output.write(str(getScore(image_url)) + "\t")
    # sleep(0.5)
    image_url = "https://raw.githubusercontent.com/emanhamed/Houses-dataset/master/Houses%20Dataset/" + str(i) +"_frontal.jpg"
    output.write(str(getScore(image_url)) + "\n")
    # sleep(0.5)

    print("imagen ", str(i))

output.close()



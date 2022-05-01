import requests
""""""
url = 'https://api-us.restb.ai/vision/v2/multipredict'
payload = {
    # Add your client key
    'client_key': "55f22dc5ceaa6f6b57a9081106ce43c7aef5707d1812fac6ac4cb9c425cf843a",
    'model_id': 're_condition',
    # Add the image URL you want to process
    'image_base64': "a"
}

# Make the segmentation request
response = requests.get(url, params=payload)

# The response is formatted in JSON
json_response = response.json()
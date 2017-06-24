import requests
import base64
import json

def spoofDetection(pictureStream):
    headers = {
       "x-api-key":"vOjf0XRyf72QJzFOVxff7aKYtUeRBtgR6MXAMzPe",
       "Content-Type":"image/jpeg",
    }
    url = "https://api.chui.ai/v1/spdetect"
    r  = requests.post(url,data=pictureStream,headers=headers)
    print(r.json())

# Enroll a new user. Params(3 pictures) returns enrollment
def enrollUser(img0, img1, img2, name):
    headers = {
       "x-api-key":"vOjf0XRyf72QJzFOVxff7aKYtUeRBtgR6MXAMzPe",
       "Content-Type":"application/json",
    }
    url = "https://api.chui.ai/v1/enroll"
    data = {
    "img0":base64.b64encode(img0),
    "img1":base64.b64encode(img1),
    "img2":base64.b64encode(img2),
    "name":name
    }

    r = requests.post(url, data=json.dumps(data), headers = headers)

    print(r.json())







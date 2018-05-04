from main import *
from flask import Flask, request
from random import randint
import requests, json
import cv2

app = Flask(__name__)
app.secret_key = str(randint(1000, 10000))



# set the api to perform face recognition of certain celebs
@app.route('/api/face_recognition', methods=['POST'])
def face_recognition():

    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # pass the image to the face recognition method
    result = main(img, ready=True)

    message  = {
        "data" : result
    }

    return json.dumps(message)


if __name__=="__main__":
    app.run(port=5030)





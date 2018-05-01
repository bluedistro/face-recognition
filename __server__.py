from main import *
from flask import Flask, request
from random import randint
import requests, json

app = Flask(__name__)
app.secret_key = str(randint(1000, 10000))



# set the api to perform face recognition of certain celebs
@app.route('/api/face_recognition', methods=['GET', 'POST'])
def face_recognition():

    if request.method == 'POST':
        content = request.get_json(force=True, silent=True)
        # this variable will contain an image file
        image = content['image_data']
        # pass the image to the face recognition method
        result = main(image)
        #
        message  = {
            "data" : result
        }

        return json.dumps(message)


if __name__=="__main__":
    app.run(port=5030)





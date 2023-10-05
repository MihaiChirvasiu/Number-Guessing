import random

from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

start = 0
end = 100
number = random.randint(start, end)


@app.route("/send", methods=['POST'])
def send_number():
    received_number = int(request.get_json())
    if received_number > number:
        return {"message": "Number is too big"}
    elif received_number < number:
        return {"message": "Number is too small"}
    else:
        return {"message": "You got it!"}


@app.route("/range", methods=['POST'])
def change_range():
    data = request.get_json()
    to = int(data['toS'])
    fro = int(data['fromS'])
    global number
    number = random.randint(to, fro)
    return {"message": "Generated number!"}


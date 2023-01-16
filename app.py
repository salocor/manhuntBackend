import json
from flask import Flask, jsonify, request
import requests as rq
app = Flask(__name__)

data = { };
data["location"] = {
        "latitude": -1,
        "longitude": -1
        }

@app.route('/location', methods=['GET'])
def putLocation():
    data["location"] = {
        "latitude": request.args.get("lat"),
        "longitude": request.args.get("long")
        }
    print("hiderLat: " + str(hiderLat) + " hiderLong: " + str(hiderLong))

@app.route('/getLocation', methods=['GET'])
def getLocation():
    return jsonify(data);

app.run(host = '0.0.0.0', ssl_context='adhoc')


#url scheme: http://localhost:5000/location?lat=10&long=9

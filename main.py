from flask import Flask
from dotenv import load_dotenv
import requests
from flask_cors import CORS

load_dotenv()
url = "https://api.nasa.gov/planetary/apod?api_key="
import os

key = os.environ["api_key"]
app = Flask(__name__)
CORS(app)

@app.route("/api/nasa", methods=["GET"])
def get_photo():
    response = requests.get(url + key)
    response.raise_for_status
    #print("API response received")
    data = response.json()
    return data

@app.route("/")
def index():
    return "i hate myself"
app.run(host="0.0.0.0", port=8005, debug=True)

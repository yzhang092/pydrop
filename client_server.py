from flask import jsonify
from flask import Flask
from flask import render_template
import json
import requests
from src.file_cart import FileCart

app = Flask(__name__)


# Home page of client server with a button to start fetch files
@app.route("/")
def index():
    return render_template('client_index.html')


# The page shows the progress of fetching
@app.route("/fetch")
def client_fetch():
    return render_template('client_file_status.html')


# The API that start the process fetching files
@app.route("/fetch_file")
async def client_fetch_file():
    engine_file_list = json.loads(requests.get('http://localhost:5000/check').content)
    file_cart = FileCart(engine_file_list['data'])
    client_file_list = file_cart.get_client_file_list()
    await file_cart.fetch_missing()
    return jsonify({"engine": engine_file_list, "client": client_file_list})

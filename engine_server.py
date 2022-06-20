from flask import Flask
from flask import render_template
from flask import jsonify
from flask import send_from_directory
from src.file_engine import FileEngine

app = Flask(__name__)


# Home page of server 1
@app.route("/")
def index():
    return render_template('engine_index.html')


# the API that starts generating files
@app.route("/start")
def engine_start():
    new_engine = FileEngine(100)
    new_engine.start()
    return jsonify({"msg": "Engine Started..."})


# Page that shows the progress
@app.route("/status")
def engine_status():
    return render_template('engine_file_status.html')


# API used to get the current progress, called in /status page
@app.route("/check")
def engine_check():
    check_engine = FileEngine(100)
    return jsonify({"data": sorted(check_engine.status(), key=float)})


# API that response the file.
# TODO: This is the file server so load balancer and other methods should be used to handle multiple request.
#  Should this part also written in async?
# @app.route("/fetch/<filename>")
# def engine_fetch_file(filename):
#     file_dir = './engineDir'
#     try:
#         return send_from_directory(file_dir, filename, as_attachment=True)
#     except FileNotFoundError:
#         return jsonify({"msg": "File not found.."})

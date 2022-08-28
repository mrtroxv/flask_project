import json
from flask import request, Flask
import requests
app = Flask(__name__)

# i use post man to test this api


@app.route('/', methods=['GET'])
def speak():
    r = requests.get("https://musika-api.herokuapp.com/")
    return r.json()


@app.route('/song/trending', methods=['GET'])
def speak_trending():
    req = request.json
    r = requests.get(
        f"https://musika-api.herokuapp.com/songs/trending/{req['page_number']}")
    return r.json()


@app.route('/search', methods=['GET'])
def speak_search():
    pyload = request.json
    r = requests.get(
        f"https://musika-api.herokuapp.com/songs/search", params=pyload)
    return r.json()


@app.route('/song/popular', methods=['GET'])
def speak_popular():
    req = request.json
    r = requests.get(
        f"https://musika-api.herokuapp.com/songs/popular/{req['page_number']}")
    return r.json()


@app.route('/song/new', methods=['GET'])
def speak_new():
    req = request.json
    r = requests.get(
        f"https://musika-api.herokuapp.com/songs/new/{req['page_number']}")
    return r.json()


@app.route('/song', methods=['GET'])
def speak_song():
    req = request.json
    r = requests.get(f"https://musika-api.herokuapp.com/song/{req['song_id']}")
    return r.json()


app.run(debug=True)

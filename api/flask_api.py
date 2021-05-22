#!/usr/bin/env python

'''API library to authenticate user and make spotify API requests'''

import os
import json
from urllib.parse import quote
import requests
import json
from flask import Flask, request, redirect, render_template, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from spotify_api import add_playlist, add_to_playlist, get_playlists, get_songs
from user import User

# Code taken partially from https://github.com/drshrey/spotify-flask-auth-example

load_dotenv()
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

SPOTIFY_AUTH_URL = "https://accounts.spotify.com/authorize"
SPOTIFY_TOKEN_URL = "https://accounts.spotify.com/api/token"
SPOTIFY_API_BASE_URL = "https://api.spotify.com/v1"

REDIRECT_URI = "http://localhost:8000/callback/q"
SCOPE = "playlist-read-private playlist-read-collaborative playlist-modify-public playlist-modify-private user-library-read"
TOKEN = ""

auth_query_parameters = {
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
    "client_id": CLIENT_ID
}


def create_playlist(data: dict):

    ''' Creates a playlist in user's spotify account'''

    if 'user' not in data:
        return "Please enter user", 400
    if 'name' not in data:
        return "Please enter name of playlist as name", 400
    if TOKEN == "":
        return "Please authenticate your account by going to http://localhost:8000", 400
    name = data['name']
    user = data['user']
    res = add_playlist(TOKEN, user, name)
    if res:
        return f"Successfully created playlist with name {name} for user {user}", 200
    return f"Failed to create playlist with name {name} for user {user}", 400


def put_songs(data: dict):

    ''' Adds songs to playlist in user's account'''

    if 'user' not in data:
        return "Please enter user", 400
    if 'playlist_id' not in data:
        return "Please enter id of playlist to be updated", 400
    if 'tracks' not in data or type(data['tracks']) != list:
        return "Please enter track ids as list", 400
    if TOKEN == "":
        return "Please authenticate your account by going to http://localhost:8000", 400

    id = data['playlist_id']
    user = data['user']
    res = add_to_playlist(TOKEN, user, id, data['tracks'])

    if res:
        return f"Successfully added songs to playlist with id {id}", 200
    return f"Failed to add songs to playlist with id {id}", 400


def create_app():

    ''' Creates and defines the flask app'''

    app = Flask(__name__)
    cors = CORS(app)
    app.config['CORS_HEADER'] = 'Content-Type'

    @app.route("/authenticate")
    def index():
        url_args = "&".join([f"{key}={quote(val)}" for key, val in auth_query_parameters.items()])
        auth_url = f"{SPOTIFY_AUTH_URL}/?{url_args}"
        return redirect(auth_url)


    @app.route("/callback/q")
    def callback():
        auth_token = request.args['code']
        code_payload = {
            "grant_type": "authorization_code",
            "code": str(auth_token),
            "redirect_uri": REDIRECT_URI,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        }
        res = requests.post(SPOTIFY_TOKEN_URL, data=code_payload)

        res = res.json()
        global TOKEN
        TOKEN = res["access_token"]
        print("ACCESS TOKEN: " + str(TOKEN))
        return render_template("index.html")


    @app.route("/create", methods = ['POST'])
    def api_create_playlist():

        ''' Creates a playlist in user's spotify account'''

        if request.content_type != "application/json":
            return "Please enter JSON into request body", 415

        data = json.loads(request.data.decode("utf-8").replace("\'", "\""))

        return create_playlist(data)


    @app.route("/create_add", methods = ['POST'])
    def api_create_add_playlist():

        ''' Creates a playlist in user's spotify account and
            adds provided tracks'''

        if request.content_type != "application/json":
            return "Please enter JSON into request body", 415
        data = json.loads(request.data.decode("utf-8").replace("\'", "\""))

        res = create_playlist(data)
        if res[1] != 200:
            return res[0], 400

        playlists = get_playlists(data['user'])

        id = None
        for playlist in playlists:
            if playlist['name'] == data['name']:
                id = playlist['id']
                break

        if id == None:
            return "Playlist not found", 400
        data['playlist_id'] = id

        return put_songs(data)


    @app.route("/playlist/create_recommended", methods=['POST'])
    def api_create_recommended_songs_playlist():

        if request.content_type != "application/json":
                return "Please enter JSON into request body", 415

        data = json.loads(request.data.decode("utf-8").replace("\'", "\""))

        if TOKEN == "":
            return "Please authenticate your account by going to http://localhost:8000", 400
        if 'user' not in data:
            return "Please enter user", 400
        if 'name' not in data:
            return "Please enter name of playlist as name", 400
        if 'length' not in data:
            return "Please enter length of playlist as length", 400
        name = data['name']
        length = data['length']
        try:
            length = (int)(length)
        except:
            return f"Length {length} is not an integer", 400
        username = data['user']
        u = User(username)
        rec_songs = u.get_recommended_songs(TOKEN)
        if rec_songs == None:
            return f"Failed to get recommended songs for user {username}", 400
        print(json.dumps(rec_songs, indent=4))
        if not u.add_playlist(name, TOKEN):
            return f"Failed to create playlist with name {name} for user {username}", 400
        playlists = u.get_playlists(TOKEN)
        songs_added = []
        total_length = 0
        for playlist in playlists:
            if playlist.get_name() == name:
                for song in rec_songs:
                    if total_length >= length:
                        break
                    total_length += song['duration_ms']/(1000*60)
                    uri = song['uri']
                    playlist.add_song(uri, TOKEN)
                    songs_added.append(song)
                break
        return json.dumps(songs_added), 200
        if res:
            return f"Successfully created playlist with name {name} for user {user}", 200
        return f"Failed to create playlist with name {name} for user {user}", 400


    @app.route("/songs", methods = ['GET'])
    def api_get_songs():

        ''' Gets songs using method in spotify api'''

        if request.content_type != "application/json":
            return "Please enter JSON into request body", 415

        data = json.loads(request.data.decode("utf-8").replace("\'", "\""))
        res = get_songs(data)
        if len(res) == len(data.keys()):
            return jsonify(res), 200
        return jsonify(res), 400


    @app.route("/add", methods = ['PUT'])
    def api_add_to_playlist():

        ''' Adds songs to playlist in user's account'''

        if request.content_type != "application/json":
            return "Please enter JSON into request body", 415
        data = json.loads(request.data.decode("utf-8").replace("\'", "\""))
        return put_songs(data)


    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=8000)

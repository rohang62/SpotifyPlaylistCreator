#!/usr/bin/env python

'''Library used to make requests to spotify web api
   (getting songs/playlist and posting to account)'''

import os
import sys
import requests
import json
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

load_dotenv()
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

def get_auth_headers():

    ''' Creates and returns authorization header for requests'''

    url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(url, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return {
      'Authorization': 'Bearer {token}'.format(token=access_token)
    }


def add_song_to_playlist(playlist_id: str, song_uri: str, token: str) -> bool:
    url = 'https://api.spotify.com/v1/playlists/' + str(playlist_id) + '/tracks?uris=' + str(song_uri)
    res = requests.post(url, headers={
        'Authorization': 'Bearer {token}'.format(token=token)
    })
    data = res.json()
    print(json.dumps(data, indent=4))
    return data


def get_recommended_songs(seed_artist: str, token: str) -> dict:
    '''
    Gets list of liked songs from spotify api
    '''
    songs = []
    url = 'https://api.spotify.com/v1/recommendations?market=US&min_popularity=50&limit=100&seed_artists=' + seed_artist
    print("FINAL URL: " + str(url))
    res = requests.get(url, headers={
        'Authorization': 'Bearer {token}'.format(token=token)
    })
    data = res.json()
    try:
        for item in data['tracks']:
            songs.append(item)
    except:
        print("get_recommended_songs() failed. Response: " + str(json.dumps(data, indent=4)))
    return songs


def get_songs(song_details: dict) -> list:

    ''' Gets list of songs from spotify api
        params - song_details (dict with track name as key and track artist as value)
        returns list of song ids'''

    songs = []
    for track_name in song_details.keys():
        try:
            url = 'https://api.spotify.com/v1/search'
            url += f'?q=artist:{song_details[track_name]} track:{track_name}&type=track'
            res = requests.get(url, headers=get_auth_headers())
            songs.append(res.json()['tracks']['items'][0]['id'])
            print(f"Successfully retrieved track {track_name} artist {song_details[track_name]}")
        except:
            print("Unexpected error:", sys.exc_info()[0])
    return songs


def get_playlists(user: str, token: str) -> dict:

    ''' Gets list of playlists from spotify api
        params - user (account username)
        returns dictionary with key as playlist name and value as playlist id'''

    try:
        url = f'https://api.spotify.com/v1/users/{user}/playlists'
        res = requests.get(url, headers=get_auth_headers())
        res = res.json()
        return res['items']
    except:
        print("Unexpected error:", sys.exc_info()[0])
    return []


def add_playlist(token: str, user: str, name: str) -> bool:

    ''' Creates playlist in user's accounts
        params - token (token for spotify client)
                 user (username for account to add playlist)
                 name (name of playlist to add)'''

    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                          client_secret=CLIENT_SECRET)
    spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                                     auth = token)
    try:
        spotify_client.user_playlist_create(user, name)
        print(f"Successfully created playlist for user {user} with name {name}")
        return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False

def add_to_playlist(token: str, user: str, playlist_id: str, track_ids: list) -> bool:

    ''' Creates playlist in user's accounts
        params - token (token for spotify client)
                 user (username for account to add playlist)
                 playlist_id (id of playlist to add tracks to)
                 track_ids (ids for tracks to add)'''

    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID,
                                                          client_secret=CLIENT_SECRET)
    spotify_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                                     auth = token)
    try:
        spotify_client.user_playlist_add_tracks(user, playlist_id, track_ids)
        print(f"Successfully added tracks to playlist with id {playlist_id}")
        return True
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return False


def get_liked_songs(token: str) -> list:
    '''
    Gets list of liked songs from spotify api
    '''
    songs = []
    url = 'https://api.spotify.com/v1/me/tracks'
    res = requests.get(url, headers={
        'Authorization': 'Bearer {token}'.format(token=token)
    })
    data = res.json()
    print(token)
    print(data)
    try:
        for item in data['items']:
            songs.append(item['track'])
    except:
        print("get_liked_songs() failed. Response: " + str(json.dumps(data, indent=4)))
        return None
    return songs

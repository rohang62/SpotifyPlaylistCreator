import requests
import spotify_api
import parser
from playlist import Playlist

'''
Class to describe a spotify user. Currently holds data for the username and playlist.
'''
class User:
  # Username from Spotify
  m_name = ""

  # The dictionary of playlist ids to playlists
  # TODO: Change to using dedicated playlist objects from Parser
  m_playlists = []
  m_liked_songs = []

  def __init__(self, username: str):
    self.m_name = username

  def add_playlist(self, name: str, token: str) -> bool:
    return spotify_api.add_playlist(token, self.m_name, name)

  def get_playlists(self, token: str):
    self.m_playlists = parser.parse_playlists(spotify_api.get_playlists(self.m_name, token))
    return self.m_playlists

  def get_name(self):
    return self.m_name

  def get_liked_songs(self, token: str):
    self.m_liked_songs = spotify_api.get_liked_songs(token)
    return self.m_liked_songs

  def get_recommended_songs(self, token: str):
    liked_songs = self.get_liked_songs(token)
    if liked_songs == None:
        return None
    self.m_liked_artists = dict()
    for song in liked_songs:
        if 'artists' not in song:
            print('Song artists not provided')
        else:
            for artist in song['artists']:
                if 'id' in artist:
                    artist_id = artist['id']
                    if artist_id in self.m_liked_artists:
                        self.m_liked_artists[artist_id] += 1
                    else:
                        self.m_liked_artists[artist_id] = 1
    ordered_artists = []
    for k, v in self.m_liked_artists.items():
        ordered_artists.append((v, k))
    ordered_artists.sort(reverse=True)
    if len(ordered_artists) > 0:
        return spotify_api.get_recommended_songs(ordered_artists[0][1], token)
    return None

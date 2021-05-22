import spotify_api

'''
Class used to represent a playlist
'''

class Playlist:
  m_id = "[ID NOT PARSED]"
  m_name = "[NAME NOT PARSED]"
  m_owner = "[OWNER_NAME NOT PARSED]"
  m_description = "[DESCRIPTION NOT PARSED]"
  m_tracks_url = "[TRACKS URL NOT PARSED]"
  m_tracks = []

  '''
  All fields will be provided at time of construction
  '''
  def __init__(self, pid: str, name: str, owner: str, description: str, tracks_url: str):
    self.m_id = pid
    self.m_name = name
    self.m_owner = owner
    self.m_description = description
    self.m_tracks_url = tracks_url

  '''
  Basic getters
  '''
  def get_name(self):
    return self.m_name

  def get_id(self):
    return self.m_id

  def get_owner(self):
    return self.m_owner

  def get_description(self):
    return self.m_description

  def get_tracks_url(self):
    return self.m_tracks_url

  def get_tracks(self):
    m_tracks = spotify_api.get_songs_from_playlist(self.m_tracks_url)
    return m_tracks

  def add_song(self, song_uri: str, token: str):
    spotify_api.add_song_to_playlist(self.m_id, song_uri, token)

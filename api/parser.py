from playlist import Playlist

'''
Used to take a playlist returned by the API and turn it into a playlist object
'''
def parse_playlists(playlists: dict) -> list:
  ret = []
  for playlist in playlists:
    try:
      parsed_playlist = Playlist(playlist['id'], playlist['name']
        , playlist['owner']['display_name'], playlist['description']
        , playlist['tracks']['href']
      )
      ret.append(parsed_playlist)
    except:
      print("Invalid playlist dictionary. Invalid playlist: " + str(playlist))
      return []
  return ret

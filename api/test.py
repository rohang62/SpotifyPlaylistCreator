from user import User
import spotify_api

u = User("oliveguyx")
playlists = u.get_liked_songs()
print(len(playlists))

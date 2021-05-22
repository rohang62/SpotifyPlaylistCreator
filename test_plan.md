To test this library, please ensure you have flask, spotipy and dotenv installed on your computer.

Next, please go to developer.spotify.com and create an app to retrieve your client id and client secret. Once you have these, keys, set your environment variables CLIENT_ID and CLIENT_SECRET.

After this is done, you can go into the directory and run 'python api/flask_api.py'

# GET

When using get, the endpoint is /songs. Pass in the request into the request body as a dictionary with keys as the song names, and values as the author for the song. Here, by passing in a dictionary with one key and value, we receive one song id that can be used to update the playlist.

![](testplan_images/get_one.jpg)

If we pass in multiple song names with artists, we should see the following screen:

![](testplan_images/get_multiple.jpg)

If we pass in a single invalid entry, we should see the following screen since the id won't exist:

![](testplan_images/get_invalid.jpg)

As shown in the image, the request would return a status of 400.

# POST

When using POST, the enpoint is either /create or /create_add depending on whether or not you want to post an empty playlist or a playlist with songs.

When using /create, first ensure you have gone to http://localhost:8000 to authenticate your account. If you do not do this, you will see the following screen:

![](testplan_images/post_authenticate.jpg)

If you go to that url, you should see the following screen:

![](testplan_images/login.jpg)

Please log in to spotify. After logging in, you will be asked to provide permissions for the app as follows:

![](testplan_images/authenticated.jpg)

Once this step is done, you can go back and make the post request. By passing in a valid username and playlist name, you should see the following screen:

![](testplan_images/create_res.jpg)

If you go to your spotify account, you should see the playlist created:

![](testplan_images/spotify.jpg)

As shown in the left column, we can see the newly created playlist called 'hi'.

If we use the /create_add endpoint, you need to also pass in the track_ids as a list. This endpoint also requires the user authentication as shown for the /create endpoint. If you pass in all of these, you should see the following screen:

![](testplan_images/create_add.jpg)

If you look at your spotify account, you should see the newly created playlist again on the left named 'test':

![](testplan_images/spotify_test.jpg)

If you click on the playlist, you should see the song Better by Khalid since that is the track id we passed in.

![](testplan_images/actual_playlist.jpg)

If you forget to pass in tracks or pass it in as some format other than a list, you should see the following screen:

![](testplan_images/tracks_pass.jpg)

The same thing would happen for both endpoints if you forget to pass in user or name:

![](testplan_images/user.jpg)

# PUT

When using put, the endpoint is /add. Pass in the request into the request body as a dictionary and make sure to pass in the username, the playlist id and the track ids as a list. You can see the output below for adding one song to a playlist:

![](testplan_images/put_one.jpg)

If you go to the spotify account and click on the playlist, you should now see the song in the playlist:

![](testplan_images/spotify_put.jpg)

If you pass in multiple song ids, you should see the following screen:

![](testplan_images/put_one.jpg)

If you go to the spotify account and click on the playlist, you should now see all the songs in the playlist:

![](testplan_images/put_multiple.jpg)

# Website

To run the website, go to the web directory and run the command `npm start`. Make sure to also run the file flask_api.py using the command `python api/flask_api.py` from the project root directory. This allows the website to make requests.

Once the website is started, by going to `localhost:3000`, you should see the login screen.

![](testplan_images/login_screen.jpg)

If the details provided are incorrect, you should see the following screen:

![](testplan_images/incorrect_login_screen.jpg)

If the provided details are correct, it should redirect you to spotify to login provide permissions as shown below:

![](testplan_images/authentication.jpg)

Once you have provided the permissions, you should see the following screen, upon which you should return to the website:

![](testplan_images/done.jpg)

When you go back to the website, you should see an input for the name of the playlist as well as a slider indicating how long the playlist should be:

![](testplan_images/user_input.jpg)

The create playlist button is disabled until a name is given for the playlist. After providing a name for the playlist and setting the time, you can click create playlist, which should redirect you to the playlist view page. While the request is being processed you should see a loading screen as shown:

![](testplan_images/loading.jpg)

Once the playlist is created and the response is received, you should see the following screen displaying all the songs added to the new playlist created:

![](testplan_images/final.jpg)

You can also see the playlist created in the spotify account. I set the time to 200 minutes and you as you can see, the playlist time is within 5 minutes of that. (3 * 60 + 22 = 202)

![](testplan_images/account.jpg)

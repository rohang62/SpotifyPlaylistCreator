This repo contains code for creating an app that can create Spotify playlists.

For week 1, Rohan's objective was to connect to the Spotify API and have user authentication working. This can be seen in the flask_api.py file under the api directory.

By running this file and going to localhost:8000, the user is redirected to Spotify's user authentication where they can login and give permissions. They can then go back and make a request using postman to the endpoint localhost:8000/create to create an empty playlist in their account.  

User authentication is not required to test getting songs or playlists, as those actions in the spotify API do not require user permissions, however, to have any of this working, a user will have to create an app on the spotify developer console, set the redirect URI to localhost:8000 and set their environment variables CLIENT_ID and CLIENT_SECRET to what is shown in the dashboard.

For week 2, Rohan's objective was to complete the flask api functionality, making it possible to get songs, post empty and actual playlists, and add songs to playlist using PUT. The PUT and POST methods still require user authentication but the GET endpoint doesn't.

For next week, Rohan will create the basic app with the login screen, incorrect login page, a screen to enter desired playlist length, loading screens, screen to show playlist was created and error handling for all views. He will also work on transitioning between the views and have a responsive layout.

For week 3, Rohan's objective was to create the base website with the login screen, incorrect login page, a screen to enter desired playlist length, loading screens, screen to show playlist was created and error handling for all views. Rohan also worked on transitioning between views and having a responsive layout. This can be tested by going into the directory 'web' and running npm start. From there, you can login and then do the spotify authentication. After that, you should be sent to the user input page, where you can put in the playlist name and length of playlist. This should lead to the view page which displays the output.

For the last week, Rohan worked on completing the webpage and integrating it with the code written by Sankalp to have a fully functioning website. The results can be seen in the manual test plan.

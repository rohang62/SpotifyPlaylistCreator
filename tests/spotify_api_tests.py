#!/usr/bin/env python

'''Spotify API test module'''

import unittest
from api.spotify_api import add_playlist, get_playlists, \
get_songs, add_to_playlist

class TestSpotifyAPI(unittest.TestCase):

    '''Test class'''

    def test_invalid_get_songs(self):

        '''Tests getting songs with invalid names and artists'''

        self.assertEqual(get_songs({"abc" : "xyz"}), [])


    def test_valid_get_song(self):

        '''Tests getting one song with valid name and artist'''

        self.assertEqual(get_songs({"Better" : "Khalid"}),
                         ['6zeeWid2sgw4lap2jV61PZ'])


    def test_valid_get_songs(self):

        '''Tests getting multiple songs with valid names and artists'''

        self.assertEqual(get_songs({"Better" : "Khalid", "Circles" : "Post Malone"}),
                         ['6zeeWid2sgw4lap2jV61PZ', '21jGcNKet2qwijlDFuPiPb'])


    def test_invalid_get_playlists(self):

        '''Tests getting invalid playlists'''

        self.assertEqual(get_playlists(""), [])


    def test_valid_get_playlists(self):

        '''Tests getting all user playlists'''
        self.assertEqual(get_playlists("rohangoel62")[0]['name'],
                         'test')


    def test_invalid_add_playlist(self):

        '''Tests invalid add playlist'''

        self.assertFalse(add_playlist("rohangoel62", "", ""))


    def test_invalid_add_to_playlist(self):

        '''Tests invalid add to playlist'''

        self.assertFalse(add_to_playlist("", "rohangoel62", "", []))

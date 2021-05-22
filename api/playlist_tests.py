import unittest
from playlist import Playlist

class TestApp(unittest.TestCase):
  def setUp(self):
    self.base_playlist = Playlist("TEST_ID", "TEST_NAME", "TEST_OWNER", "TEST_DESCRIPTION", "TEST_TRACKS")

  def test_name(self):
    self.assertEqual(self.base_playlist.get_name(), "TEST_NAME")

  def test_id(self):
    self.assertEqual(self.base_playlist.get_id(), "TEST_ID")

  def test_owner(self):
    self.assertEqual(self.base_playlist.get_owner(), "TEST_OWNER")

  def test_description(self):
    self.assertEqual(self.base_playlist.get_description(), "TEST_DESCRIPTION")

  def test_tracks_url(self):
    self.assertEqual(self.base_playlist.get_tracks_url(), "TEST_TRACKS")

def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApp))
  return suite

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(suite())

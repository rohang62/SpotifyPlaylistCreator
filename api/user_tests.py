import unittest
from user import User
from dotenv import load_dotenv
import os
TOKEN = os.getenv('CS242_TOKEN')

class TestApp(unittest.TestCase):
  def setUp(self):
    self.base_user = User("oliveguyx")

  def test_name(self):
    self.assertEqual(self.base_user.get_name(), "oliveguyx")

  def test_add_playlist(self):
    self.assertEqual(self.base_user.add_playlist(TOKEN, "TEST_PLAYLIST"), True)
    
  def test_get_playlists(self):
    self.assertEqual(len(self.base_user.get_playlists()) > 1, True)

  def test_get_liked_songs(self):
    self.assertEqual(len(self.base_user.get_liked_songs()), 20)



def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestApp))
  return suite

if __name__ == '__main__':
  unittest.TextTestRunner(verbosity=2).run(suite())

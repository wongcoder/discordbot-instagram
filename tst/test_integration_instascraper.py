import logging
import unittest

import src.instascraper as instascraper

# Do not rely on these tests outside of testing cookies. Unit tests are to test functionality.
class test_integration_instascraper(unittest.TestCase):
  SEARCHED_TAG = "apple"

  URL = 'https://www.instagram.com/explore/tags/'+ SEARCHED_TAG + '/?__a=1'
  AUTHOR_URL = "https://www.instagram.com/p/B7YdRpPHzRj/"

  def test_rotate_cookie(self):
    self.assertIsNotNone(instascraper.random_cookie())

  def test_query_instagram(self):
    query = instascraper.query_instagram(self.URL)
    self.assertIsNotNone(query)

  def test_get_post(self):
    self.assertIsNotNone(instascraper.get_post(self.SEARCHED_TAG))


  def test_get_author(self):
    self.assertIsNotNone(instascraper.get_author(self.AUTHOR_URL))
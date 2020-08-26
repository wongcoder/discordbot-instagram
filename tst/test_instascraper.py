import logging
import unittest
import requests
import json
from unittest.mock import MagicMock, patch

from src.instascraper import get_post, get_author, get_post, query_instagram

class test_instascraper(unittest.TestCase):
  SEARCHED_TAG = "apple"
  AUTHOR_URL = "https://www.instagram.com/p/B7YdRpPHzRj/"

  AUTHOR_ID = "123"
  POST_NODE = {"mocked": "True"}

  MOCKED_POST_JSON = {
    "graphql": {
      "hashtag": {
        "edge_hashtag_to_media": {
          "edges": [
            {
              "node": POST_NODE 
            }
          ]
        }
      }
    }
  }


  MOCKED_AUTHOR_JSON = {
    "graphql": {
      "shortcode_media": {
        "owner": {
          "id": AUTHOR_ID 
        }
      }
    }
  }

  class MockResponse:
    encoding = True
    content = True

    def __init__(self, text):
      self.text = json.dumps(text)

  # Check intended behavior of functions
  @patch('src.instascraper.requests.request') 
  def test_query_instagram(self, mock):
    mock.return_value = MagicMock(ok=True) 
    mock.return_value.json.return_value = self.MOCKED_AUTHOR_JSON

    json = query_instagram(self.AUTHOR_URL)
    self.assertEqual(json, self.MOCKED_AUTHOR_JSON)

  @patch('src.instascraper.query_instagram')
  def test_get_post(self, mock):
    mock.return_value = self.MOCKED_POST_JSON
    post = get_post(self.SEARCHED_TAG)
    self.assertEqual(self.POST_NODE, post)
  
  @patch('src.instascraper.query_instagram') 
  def test_get_author(self, mock):
    mock.return_value = self.MOCKED_AUTHOR_JSON

    author = get_author(self.AUTHOR_URL)
    self.assertEqual(self.AUTHOR_ID, author)

  # Check how functions respond on outages
  @patch('src.instascraper.requests.request')
  def test_get_post_outage(self, mock):
    mock.return_value = MagicMock()
    mock.return_value.json.return_value = None
    self.assertIsNone(get_post(self.SEARCHED_TAG))

  @patch('src.instascraper.requests.request')
  def test_get_author_outage(self, mock):
    mock.return_value = MagicMock()
    mock.return_value.json.return_value = None
    self.assertIsNone(get_author(self.SEARCHED_TAG))

  @patch('src.instascraper.requests.request')
  def test_query_instagram_outage(self, mock):
    mock.return_value = MagicMock()
    mock.return_value.json = "NOT A JSON"
    self.assertRaises(TypeError, query_instagram(self.AUTHOR_URL))
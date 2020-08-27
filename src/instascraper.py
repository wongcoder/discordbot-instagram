# Used InstaData as a frame of reference https://github.com/hindamosh/InstaData

import os, sys, requests, logging, random
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def random_cookie():
    cookie = None
    try: 
        cookies = os.getenv("COOKIE").split(',')
        index = random.randint(0, len(cookies)-1)
        cookie = cookies[index]
    except:
        logging.exception("Your COOKIE is probably misconfigured.")
        raise

    return cookie

# internal function used to make instagram call 
def query_instagram(url):
    headers = { 'Cookie': 'sessionid=' + random_cookie() }
    
    data = None

    # perform attempt to try again 
    attempt = 0
    while data is None and attempt < 10:
        attempt += 1
        try: 
            response = requests.request("GET", url, headers=headers, timeout=5)
            data = response.json()
        except: 
            logging.exception("Error occured while attempting to query URL")
    
    return data

# public
def get_post(searched_tag):
    url = 'https://www.instagram.com/explore/tags/'+ searched_tag + '/?__a=1'
    data = query_instagram(url)
    if data is None: return None

    posts = data['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    cleaned_posts = [i['node'] for i in posts]

    return cleaned_posts[0]


# Public functions
def get_author(url):
    url = url + '?__a=1'
    data = query_instagram(url)
    if data is None: return None
    
    author = data['graphql']['shortcode_media']['owner']['id']
    return author

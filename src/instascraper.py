# Used InstaData as a frame of reference https://github.com/hindamosh/InstaData

import os
import sys
import requests
from datetime import datetime
from dotenv import load_dotenv

# acquire session cookie
load_dotenv()
COOKIE = os.getenv("COOKIE")

headers = {
    'Cookie': 'sessionid=' + COOKIE
}

# Private functions
def insta_scraper(searched_tag):
    print(COOKIE)
    print('Attempting to search')
    print(datetime.now())
    url = 'https://www.instagram.com/explore/tags/'+ searched_tag + '/?__a=1'
    try:  
        # get json data from requests library
        response = requests.request("GET", url, headers=headers, timeout=5)
        data = response.json()
    except:
        print('request failed')
        return []
    else:
        posts = data['graphql']['hashtag']['edge_hashtag_to_media']['edges']
        cleaned_posts = [i['node'] for i in posts]
        return cleaned_posts
    print('Out of scope error?')
    return []


# Public functions
def author_lookup(url):
    url = url + '?__a=1'
    try: 
        response = requests.request("GET", url, headers=headers, timeout=5)
        data = response.json()
    except:
        print('exception occured', sys.exc_info()[0])
        print('author_lookup for link:' + url + 'failed')
        return '404: ID not found!'
    else:
        author = data['graphql']['shortcode_media']['owner']['id']
        return author


def get_latest_post(searched_tag):
    posts = insta_scraper(searched_tag)
    print(insta_scraper)
    while len(posts) == 0: 
        print('Posts were empty... trying again')
        posts = insta_scraper(searched_tag)
    return posts[0]


if __name__ == "__main__":
    
    # unit test insta_scraper
    print('Running insta_scraper() test')
    test = insta_scraper('apples')
    if len(test) > 0: 
        print('Passed instascraper test!') # can fail even if function works
    
    # unit test latest_post
    print('Running latest_post() test')
    latest_post = get_latest_post('balisongsale')
    print(str(latest_post))
    print('If the above wasnt None, it passed!')

    # unit test author_lookup
    print(author_lookup('https://www.instagram.com/p/B7YdRpPHzRj/'))
    print('if this was not null, test was OK. otherwise, try new post')

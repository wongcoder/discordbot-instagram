# Used InstaData as a frame of reference https://github.com/hindamosh/InstaData

import requests
from time import sleep 

# should be private but idk python syntax
def insta_scraper(searched_tag):
    url = 'https://www.instagram.com/explore/tags/'+ searched_tag + '/?__a=1'
    try:  
        response = requests.get(url, timeout=5)
    except requests.Timeout:
        print('request timed out')
        return []
    else:
        # get json data from requests library
        data = response.json()

        posts = data['graphql']['hashtag']['edge_hashtag_to_media']['edges']

        cleaned_posts = [i['node'] for i in posts]
        return cleaned_posts
    print('Out of scope error?')
    return []

# export
def get_latest_post(searched_tag):
    posts = []
    while len(posts) == 0: 
        posts = insta_scraper(searched_tag)
    if posts:
        return posts[0]
    else:
        return None


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

# Used InstaData as a frame of reference https://github.com/hindamosh/InstaData

import requests
from time import sleep 

def insta_scraper(searched_tag):
    url = 'https://www.instagram.com/explore/tags/'+ searched_tag + '/?__a=1'
    response = requests.get(url)
    data = response.json()
    # get json data from requests library
    
    posts = data['graphql']['hashtag']['edge_hashtag_to_media']['edges']

    cleaned_posts = [i['node'] for i in posts]
    return cleaned_posts

def get_latest(posts):
    if posts:
        return posts[0]
    else:
        return None

if __name__ == "__main__":
    tag = str(input('Enter the hashtag:'))
    print('Collecting data....')
    data = insta_scraper(tag)
    print('Data collection has been completed.')
    latest_post = get_latest(data)
    print('Latest post: ' + str(latest_post))
#!/usr/bin/python3
""" Reddit API client """


import pprint
import requests
from requests.models import Response

URL = 'http://reddit.com/r/{}/hot.json'

def recurse(subreddit, hot_list=[], after=None):
    """ GET all hot post """

    headers = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    
    resp = requests.get(URL.format(subreddit),
                            headers=headers, params=params)
    if resp.status_code != 200:
        return None
    data = resp.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                            for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)   
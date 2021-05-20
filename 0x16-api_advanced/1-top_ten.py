#!/usr/bin/python3
''' Reddit API client '''

import requests

def top_ten(subreddit):
    """
    prints the first 10 hot post listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'RRondon'}
    size_query = {"limit": 10}
    r = requests.get(url, params=size_query, headers=headers).json()
    children = r.get("data", {}).get("children", None)

    if children:
        for topic in children:
            print(topic.get("data").get("title"))
    else:
        print("None")

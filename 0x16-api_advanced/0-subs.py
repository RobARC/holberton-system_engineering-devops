#!/usr/bin/python3
''' Reddit API client '''

import requests


def number_of_subscribers(subreddit):
    """ Method returns the number of subscribers """

    if subreddit is None:
        return (0)
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'RRondon'}
    r = requests.get(url, headers=headers).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers

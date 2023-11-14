#!/usr/bin/python3
"""How many subs?
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent":
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    return 0

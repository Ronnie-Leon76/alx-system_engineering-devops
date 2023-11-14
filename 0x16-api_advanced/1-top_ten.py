#!/usr/bin/python3
"""Top Ten
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            print(post.get("data").get("title"))
    else:
        print(None)

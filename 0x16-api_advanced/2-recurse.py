#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the
    given subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        after = response.json().get("data").get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None

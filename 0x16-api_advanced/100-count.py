#!/usr/bin/python3
"""Count it!"""
import requests


def count_words(subreddit, word_list, after="", word_dic={}):
    """Prints a sorted count of given keywords listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":
               "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
                (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        for post in response.json().get("data").get("children"):
            for word in word_list:
                if word.lower() in post.get("data").get("title").lower():
                    if word in word_dic:
                        word_dic[word] += 1
                    else:
                        word_dic[word] = 1
        after = response.json().get("data").get("after")
        if after is None:
            if not len(word_dic) > 0:
                return
            for key, value in sorted(word_dic.items(),
                                     key=lambda item: item[1],
                                     reverse=True):
                print("{}: {}".format(key, value))
            return
        return count_words(subreddit, word_list, after, word_dic)
    else:
        return

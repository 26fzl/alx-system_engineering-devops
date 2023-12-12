#!/usr/bin/python3
'''number of subscribers '''
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers={"User-Agent": "fzl_26"})

    if response.status_code != 200:
        return 0
    else:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers

#!/usr/bin/python3
''' The Reddit API '''
import requests


def recurse(subreddit, list=[], after="", counter=0):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after, "counter": counter, "limit": 100}
    response = requests.get(url,
                            headers={"User-Agent"},
                            params=params)
    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    counter += results.get("dist")
    for x in results.get("children"):
        list.append(x.get("data").get("title"))
    if after is not None:
        return recurse(subreddit, list, after, counter)
    return list

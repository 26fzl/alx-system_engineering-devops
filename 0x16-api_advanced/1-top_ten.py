#!/usr/bin/python3
''' hot articles '''
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers={"User-Agent": "fzl_26"})
    if response.status_code != 200:
        print(None)
        return
    else:
        data = response.json()
        for x in range(10):
            print(data["data"]["children"][x]['data']['title'])
        return

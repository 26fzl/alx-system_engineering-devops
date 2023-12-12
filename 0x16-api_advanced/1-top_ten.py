#!/usr/bin/python3
''' hot articles '''
import requests


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers={"User-Agent"})
    if response.status_code != 200:
        print(None)
        return
    else:
        data = response.json()
        for x in range(10):
            print(data["data"]["children"][x]['data']['title'])
        return

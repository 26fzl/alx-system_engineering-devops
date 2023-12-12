#!/usr/bin/python3
'''Count words'''
import requests


def count_words(subreddit, word_list, f_list=[], after=None):
    user_agent = {"User-Agent": "fzl_26"}
    url = f"http://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    pst = requests.get(url, headers=user_agent)
    if after is None:
        word_list = [word.lower() for word in word_list]

    if pst.status_code == 200:
        pst = pst.json()["data"]
        af = pst["after"]
        pss = pst["children"]
        for post in pst:
            title = post["data"]["title"].lower()
            for word in title.split(" "):
                if word in word_list:
                    f_list.append(word)
        if af is not None:
            count_words(subreddit, word_list, f_list, af)
        else:
            result = {}
            for word in f_list:
                if word.lower() in result.keys():
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1],
                                     reverse=True):
                print(f"{key}: {value}")
    else:
        return

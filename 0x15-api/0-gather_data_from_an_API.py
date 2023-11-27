#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    compl = [d.get("title") for d in todo if d.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(compl), len(todo)))
    [print("\t {}".format(s)) for s in compl]

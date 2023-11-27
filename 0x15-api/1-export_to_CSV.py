#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress"""
import csv
import requests
import sys

if __name__ == "__main__":
    usr_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(usr_id)).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": usr_id}).json()

    with open("{}.csv".format(usr_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usr_id, username, d.get("completed"), d.get("title")]
         ) for d in todo]

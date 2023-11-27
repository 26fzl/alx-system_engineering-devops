#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": d.get("title"),
                "completed": d.get("completed"),
                "username": s.get("username")
            } for d in requests.get(url + "todos",
                                    params={"userId": s.get("id")}).json()]
            for s in users}, jsonfile)

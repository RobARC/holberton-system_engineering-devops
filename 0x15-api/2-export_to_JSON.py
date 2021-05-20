#!/usr/bin/python3
""" Script to export data in JSON """


import json
import requests
from sys import argv


def main(argv):
    """ module export data in JSON """

    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    user = url + '/users/{}'.format(user_id)
    todos = url + '/todos/?userId={}'.format(user_id)
    name = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()
    tasks = []

    with open('{}.json'.format(user_id), 'w+') as file:
        for todo in request_todo:
            task = {"task": todo.get('title'),
                    "completed": todo.get('completed'), "username": name}
            tasks.append(task)
        info = {user_id: tasks}
        file.write(json.dumps(info))


if __name__ == "__main__":
    main(argv)

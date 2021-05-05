#!/usr/bin/python3
""" Export data  information in CSV format. """


import requests
from sys import argv
import csv


def main(argv):
    """ According with user_id, export information in CSV format """

    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    user = url + '/users/{}'.format(user_id)
    todos = url + '/todos/?userId={}'.format(user_id)
    name = requests.get(user).json().get('username')
    request_todo = requests.get(todos).json()

    with open('{}.csv'.format(user_id), 'w+') as file:
        for todo in request_todo:
            info = '"{}","{}","{}","{}"\n'.format(
                user_id, name, todo.get('completed'), todo.get('title'))
            file.write(info)


if __name__ == "__main__":
    main(argv)

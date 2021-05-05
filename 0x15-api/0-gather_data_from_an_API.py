#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee
    ID, returns information about his/her TODO list progress. """


import requests
from sys import argv


def main(argv):
    """ Acording to user_id, show information """

    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
    user = url + '/users/{}'.format(user_id)
    todos = url + '/todos/?userId={}'.format(user_id)
    name = requests.get(user).json().get('name')
    request_todo = requests.get(todos).json()
    tasks = [task.get('title')
             for task in request_todo if task.get('completed') is True]

    print('Employee {} is done with tasks({}/{}):'.format(name,
                                                          len(tasks),
                                                          len(request_todo)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    main(argv)

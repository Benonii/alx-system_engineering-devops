#!/usr/bin/python3
''' This module contains a program that fetches data from a REST API and
    displays a fornatted version '''

import json
import requests
import sys


if __name__ == '__main__':
    user_id = sys.argv[1]
    employee = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(user_id)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id)).json()

    name = employee['name']

    completed_tasks = []
    for task in tasks:
        if task['completed'] is True:
            completed_tasks.append(task['title'])

    print("Employee {} is done with tasks({}/{}):"
          .format(employee['name'], len(completed_tasks), len(tasks)))
    for task in completed_tasks:
        print("\t{}".format(task))

    # print(employee)

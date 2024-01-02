#!/usr/bin/python3
''' This module contains a program that fetches data from a REST API and
    displays a fornatted version '''

import csv
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
    username = employee['username']
    filename = '{}.csv'.format(user_id)

    completed_tasks = []
    with open(filename, 'w', newline='') as f:
        csv_writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_ALL)

        for task in tasks:
            if task['completed'] is True:
                completed_tasks.append(task['title'])

            csv_data = [task['userId'], username,
                        task['completed'], task['title']]
            csv_writer.writerow(csv_data)

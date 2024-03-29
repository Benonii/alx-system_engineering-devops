#!/usr/bin/python3
''' This module contains a program that fetches data from a REST API and
    displays a fornatted version '''

import csv
import json
import requests
import sys


if __name__ == '__main__':
    employees = requests.get('https://jsonplaceholder.typicode.com/users/')\
                        .json()

    json_data = dict()
    for employee in employees:
        tasks = requests.get('https://jsonplaceholder.typicode.com/'
                             + 'todos?userId={}'
                             .format(employee['id'])).json()

        user_id = str(employee['id'])
        name = employee['name']
        username = employee['username']
        filename = 'todo_all_employees.json'

        completed_tasks = []
        task_list = []

        for task in tasks:
            if task['completed'] is True:
                completed_tasks.append(task['title'])

            task_dict = {
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed'],
                    }

            task_list.append(task_dict)

        json_data[user_id] = task_list

    with open(filename, 'w', newline='') as f:
        json.dump(json_data, f)

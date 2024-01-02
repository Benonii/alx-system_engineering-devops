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

    task_list = []
    for employee in employees:
        tasks = requests.get('https://jsonplaceholder.typicode.com/'
                             + 'todos?userId={}'
                             .format(employee['id'])).json()

        name = employee['name']
        username = employee['username']
        filename = 'todo_all_employees.json'

        completed_tasks = []

        for task in tasks:
            if task['completed'] is True:
                completed_tasks.append(task['title'])

            task_dict = {
                    "task": task['title'],
                    "completed": task['completed'],
                    "username": username,
                    }
            task_list.append(task_dict)

        with open(filename, 'w', newline='') as f:
            json_data = {
                    f"{employee['id']}": task_list
                    }
            json.dump(json_data, f)

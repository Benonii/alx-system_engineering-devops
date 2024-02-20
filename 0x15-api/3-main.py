#!/usr/bin/python3
"""
Check student JSON output
"""

import json
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Check user info """
    
    with open('todo_all_employees.json', 'r') as f:
        student_json = json.load(f)

    correct_json = requests.get(users_url).json()

    for correct_entry in correct_json:
        flag = 0
        for student_entry in student_json:
            if str(correct_entry['id']) == student_entry:
                flag = 1
        if flag == 0:
            print("User ID {} Found: Incorrect".format(correct_entry['id']))
            return
    
    print("All users found: OK")


if __name__ == "__main__":
    user_info()

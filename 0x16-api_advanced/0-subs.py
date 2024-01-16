#!/usr/bin/python3

import requests
import json
import sys


def number_of_subscribers(subr_name):
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subr_name),
                            headers={"User-Agent": "GetSubscriberCount"})

    data = response.json().get('data')
    if not data:
        return 0
    else:
        return data['subscribers']

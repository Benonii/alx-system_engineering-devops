#!/usr/bin/python3

''' This module contains the function number_of_subscribers '''
import requests
import json
import sys


def number_of_subscribers(subr_name):
    ''' Gets the number of subscribers of a subreddit '''
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subr_name),
                            headers={"User-Agent": "GetSubscriberCount"},
                            allow_redirects=False)

    data = response.json().get('data')
    if not data:
        return 0
    else:
        return data['subscribers']

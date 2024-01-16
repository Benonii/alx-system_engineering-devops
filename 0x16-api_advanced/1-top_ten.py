#!/usr/bin/python3

''' This module contains the function top_ten '''
import json
import requests


def top_ten(subreddit):
    ''' Gets the top ten topics of subscribers of a subreddit '''
    response = requests.get("https://www.reddit.com/r/{}/top.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "GetHotTopics"},
                            allow_redirects=False).json()

    data = response.get('data')
    if not data:
        print(None)
    else:
        titles = []
        for child in data['children']:
            print(child['data']['title'])

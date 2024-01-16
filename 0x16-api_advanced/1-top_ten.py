#!/usr/bin/python3

''' This module contains the function top_ten '''
import requests
import json


def top_ten(subreddit):
    ''' Gets the top ten topics of subscribers of a subreddit '''
    response = requests.get("https://www.reddit.com/r/{}/top.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "GetHotTopics"},
                            allow_redirects=False).json()

    data = response.get('data')
    if not data:
        return 0
    else:
        # print(data.keys())
        for child in data['children']:
            print(child['data']['title'])

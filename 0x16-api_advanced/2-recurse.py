#!/usr/bin/python3

''' This module contains the function recurse'''
import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    ''' Gets the all the hot articles in a subreddit '''
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"\
              .format(subreddit, after)

    response = requests.get(url, headers={"User-Agent": "GetHotArticles/2.0"},
                            allow_redirects=False).json()

    data = response.get('data')
    if not data:
        return None
    else:
        if 'children' in data:
            for child in data['children']:
                hot_list.append(child['data']['title'])

            after = data['after']

            return recurse(subreddit, hot_list, after)
        return hot_list

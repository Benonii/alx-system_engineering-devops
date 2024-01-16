#!/usr/bin/python3

''' This module contains the function recurse'''
import json
import requests


def recurse(subreddit, hot_list=[], page=None):
    ''' Gets the all the hot articles in a subreddit '''
    if page is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}"\
              .format(subreddit, page)

    response = requests.get(url, headers={"User-Agent": "GetHotArticles/2.0"},
                            allow_redirects=False).json()

    data = response.get('data')
    if not data:
        return hot_list
    else:
        for child in data['children']:
            hot_list.append(child['data']['title'])

        page = data['after']

        return recurse(subreddit, hot_list, page)

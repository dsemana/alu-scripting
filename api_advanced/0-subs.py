#!/usr/bin/python3
"""
0-subs
Module that queries the Reddit API and returns the total number
of subscribers for a given subreddit.

Usage:
    >>> number_of_subscribers('python')
    1040000  # Example output for existing subreddit

    >>> number_of_subscribers('this_sub_does_not_exist')
    0  # Example output for nonexisting subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the total number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers, or 0 if subreddit is invalid.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'python:0-subs:v1.0 (by /u/username)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    except requests.RequestException:
        return 0
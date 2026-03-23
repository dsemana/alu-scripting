#!/usr/bin/python3
"""Prints the first 10 hot posts of a given subreddit."""

import requests


def top_ten(subreddit):
    """Queries and prints the first 10 hot post titles of a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    for post in children[:10]:
        print(post.get('data', {}).get('title'))

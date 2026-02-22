#!/usr/bin/python3
"""Query Reddit API and print the top 10 hot post titles for a subreddit."""

import requests


def top_ten(subreddit):
    """Print top 10 hot post titles for `subreddit`, or None if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-reddit-api/1.0"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10,
        )
    except requests.RequestException:
        print("None")
        return

    if response.status_code != 200:
        print("None")
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
    except ValueError:
        print("None")
        return

    for post in posts[:10]:
        title = post.get("data", {}).get("title")
        if title is not None:
            print(title)

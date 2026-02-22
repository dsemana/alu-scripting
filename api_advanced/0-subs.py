#!/usr/bin/python3
"""0-subs module.

This module defines a function that queries Reddit's public API and
returns the total number of subscribers for a subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the subscriber count for a subreddit or 0 if invalid."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "alu-reddit-api/1.0"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10,
        )
    except requests.RequestException:
        return 0

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
    except ValueError:
        return 0

    return data.get("subscribers", 0)

#!/usr/bin/python3
"""Recursively query Reddit API and return all hot post titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return all hot post titles for `subreddit`, or None if invalid."""
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "alu-reddit-api/1.0"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10,
        )
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
    except ValueError:
        return None

    children = data.get("children", [])
    if not children and after is None:
        return None

    hot_list.extend(
        post.get("data", {}).get("title", "")
        for post in children
        if post.get("data", {}).get("title")
    )

    next_after = data.get("after")
    if next_after is None:
        return hot_list
    return recurse(subreddit, hot_list, next_after)

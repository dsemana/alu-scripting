#!/usr/bin/python3
"""Recursively count keyword occurrences in hot post titles for a subreddit."""

import requests


def _fetch_titles(subreddit, after=None, titles=None):
    """Recursively fetch all hot post titles. Return None for invalid subreddit."""
    if titles is None:
        titles = []

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
        return []

    titles.extend(
        post.get("data", {}).get("title", "")
        for post in children
        if post.get("data", {}).get("title")
    )

    next_after = data.get("after")
    if next_after is None:
        return titles
    return _fetch_titles(subreddit, next_after, titles)


def _count_in_word_list(word_list, idx=0, weights=None):
    """Recursively build keyword weights from word_list (duplicate-aware)."""
    if weights is None:
        weights = {}

    if idx >= len(word_list):
        return weights

    word = word_list[idx].lower()
    weights[word] = weights.get(word, 0) + 1
    return _count_in_word_list(word_list, idx + 1, weights)


def _count_title_words(titles, weights, title_idx=0, counts=None):
    """Recursively count keyword occurrences across all titles."""
    if counts is None:
        counts = {word: 0 for word in weights}

    if title_idx >= len(titles):
        return counts

    for token in titles[title_idx].lower().split():
        if token in counts:
            counts[token] += weights[token]

    return _count_title_words(titles, weights, title_idx + 1, counts)


def count_words(subreddit, word_list):
    """Print sorted keyword counts for subreddit hot posts."""
    titles = _fetch_titles(subreddit)
    if titles is None:
        return

    weights = _count_in_word_list(word_list)
    counts = _count_title_words(titles, weights)

    sorted_items = sorted(
        ((word, count) for word, count in counts.items() if count > 0),
        key=lambda item: (-item[1], item[0]),
    )

    for word, count in sorted_items:
        print(f"{word}: {count}")

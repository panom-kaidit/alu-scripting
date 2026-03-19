#!/usr/bin/python3
"""
3-count.py

This module queries the Reddit API recursively, parses the titles of
all hot articles for a given subreddit, and prints a sorted count
of given keywords (case-insensitive).
"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively retrieves hot posts and counts keyword occurrences.

    Args:
        subreddit (str): The subreddit name.
        word_list (list): List of keywords to count.
        after (str): Reddit pagination token.
        counts (dict): Dictionary storing word counts.
    """
    if counts is None:
        counts = {}

        # Normalize words to lowercase and initialize dictionary
        for word in word_list:
            lower_word = word.lower()
            counts[lower_word] = counts.get(lower_word, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:api_advanced:v1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            return

        data = response.json().get("data", {})
        children = data.get("children", [])

        for post in children:
            title_words = post.get("data", {}).get("title", "").lower().split()
            for word in title_words:
                clean_word = word.strip(".,!?\"'()[]{}_")
                if clean_word in counts:
                    counts[clean_word] += 1

        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)

        # Final output when recursion finishes
        sorted_counts = sorted(
            [(k, v) for k, v in counts.items() if v > 0],
            key=lambda x: (-x[1], x[0])
        )

        for word, count in sorted_counts:
            print("{}: {}".format(word, count))

    except Exception:
        return

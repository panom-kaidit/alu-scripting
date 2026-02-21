#!/usr/bin/python3
"""
1-top_ten.py

Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-api-project"}

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)

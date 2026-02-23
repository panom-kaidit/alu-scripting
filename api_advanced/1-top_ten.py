#!/usr/bin/python3
"""
Query Reddit API and print titles of first 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {
        "User-Agent": "alx-reddit-api-script/1.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        # If subreddit invalid OR redirected, print None
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {}).get("children", [])

        for post in data:
            print(post.get("data", {}).get("title"))

    except Exception:
        print(None)

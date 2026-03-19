#!/usr/bin/python3
"""
1-top_ten.py

Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for ``subreddit``.

    Requirements from the project:
    - Do **not** follow redirects (invalid subs may redirect to search).
    - On any error or invalid subreddit, print ``None``.
    """

    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    # Using api.reddit.com is a bit more lenient and avoids some geo/UA blocks.
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)
    params = {"limit": 10}
    headers = {
        "User-Agent": "linux:alu-api-project:v1.0 (by /u/anonymous)"
    }

    try:
        resp = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10,
        )

        if resp.status_code != 200:
            print(None)
            return

        children = resp.json().get("data", {}).get("children", [])
        if not children:
            print(None)
            return

        for post in children:
            print(post.get("data", {}).get("title"))

    except Exception:
        # Any network/parse error should result in the expected None output.
        print(None)

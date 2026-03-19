<<<<<<< HEAD
#!/usr/bin/python3
"""
1-top_ten.py

Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

=======
#!/usr/bin/python3
"""
1-top_ten.py

Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

>>>>>>> 8bbe0368686fcbfff2ad25d68925fa8445d93a4e
import requests


def top_ten(subreddit):
<<<<<<< HEAD
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
=======
    """Print the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

>>>>>>> 8bbe0368686fcbfff2ad25d68925fa8445d93a4e
    headers = {
        "User-Agent": "linux:alu-api-project:v1.0 (by /u/anonymous)"
    }

    try:
<<<<<<< HEAD
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
=======
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False
        )

        if response.status_code == 200:
            posts = response.json().get("data", {}).get("children", [])
            for post in posts:
                print(post.get("data", {}).get("title"))
        else:
            print(None)

    except Exception:
>>>>>>> 8bbe0368686fcbfff2ad25d68925fa8445d93a4e
        print(None)

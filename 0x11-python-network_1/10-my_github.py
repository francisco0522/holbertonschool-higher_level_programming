#!/usr/bin/python3

"""
My Github!
"""

import requests
from sys import argv

if __name__ == "__main__":
    auth = (argv[1], argv[2])
    res = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(res.json().get("id"))
    except ValueError:
        print("Not a valid JSON")

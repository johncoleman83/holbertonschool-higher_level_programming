#!/usr/bin/python3
"""
0-btcp_status.py
"""
import urllib.request


def display_request_data(the_url):
    """makes a request to specified URL & displays data on the request"""
    with urllib.request.urlopen(the_url) as response:
        html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf8')))


if __name__ == "__main__":
    """MAIN APP"""
    display_request_data("https://intranet.btcp.io/status")

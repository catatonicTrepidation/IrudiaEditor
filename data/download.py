#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import random

pfx = "~"

def download_image(url, filename):
    """
    Download image from url
    :param url: URL of image to download
    :param filename: Filename to call saved image
    """

    r = None
    try:
        r = requests.get(url)
    except requests.exceptions.Timeout as e:
         # Maybe set up for a retry, or continue in a retry loop
         # print(e)
         return False
    except requests.exceptions.TooManyRedirects as e:
        # Tell the user their URL was bad and try a different one
        print(e)
        return False
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print(e)
        return False
    except Exception as e:
        print(e)
        return False

    if r.status_code != 200:
        return False
    if not is_url_image(url):
        return False

    open(filename, 'wb').write(r.content)
    return True



def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers["content-type"] in image_formats:
        return True
    return False
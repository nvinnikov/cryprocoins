import requests
import json

from const import u_token, headers, base_url, try_url, cryptocurrency_url, OK, BAD


def _expt(response):
    if 200 <= response.status_code < 300:
        return response.json()
    else:
        return Exception(BAD)

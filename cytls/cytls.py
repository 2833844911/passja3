import requests
import json as jn
from urllib.parse import urlencode
import urllib

def get(url, headers=None, proxies=None, params=None, cookies=None, timeout=40, http2=False, allow_redirects=True):
    if params != None:
        url = url.split("?")[0]
        url = f'{url}?{urlencode(params)}'

    if headers == None:
        headers = {}

    if proxies == None:
        print("Please bring your proxy IP address!!!")
        return

    if "http" in proxies:
        proxies = proxies['http'].split('/')[-1].strip()
    if "https" in proxies:
        proxies = proxies['https'].split('/')[-1].strip()
    if cookies != None:
        headers["Cookie"] = '; '.join([f'{k}={v}' for k, v in cookies.items()])
    if allow_redirects == True:
        cancdx = "1"
    else:
        cancdx = "0"
    dt = {
        "cancdx": cancdx,
        "method": "GET",
        "url": url,
        "headers": headers,
        "timeout": timeout,
        "postData": "",
        "proxy": "http://"+proxies,
        "http2": http2
    }
    ud =  "http://103.71.69.97:28080/request"
    response = requests.post(ud, json=dt, timeout=timeout, allow_redirects=False)
    return response


def post(url, headers=None, proxies=None, params=None, cookies=None, json=None, data=None, timeout=40, http2=False,
         allow_redirects=True):
    if params != None:
        url = url.split("?")[0]
        url = f'{url}?{urlencode(params)}'

    if headers == None:
        headers = {}
    if type(data) == type({}):
        data = urllib.parse.urlencode(data)

    if proxies == None:
        print("Please bring your proxy IP address!!!")
        return

    if "http" in proxies:
        proxies = proxies['http'].split('/')[-1].strip()
    if "https" in proxies:
        proxies = proxies['https'].split('/')[-1].strip()
    if cookies != None:
        headers["Cookie"] = '; '.join([f'{k}={v}' for k, v in cookies.items()])
    postData = ""
    if data != None:
        postData = data
    if json != None:
        postData = jn.dumps(json)
        headers['Content-Type'] = 'application/json'

    if allow_redirects == True:
        cancdx = "1"
    else:
        cancdx = "0"
    dt = {
        "cancdx": cancdx,
        "method": "POST",
        "url": url,
        "headers": headers,
        "postData": postData,
        "timeout": timeout,
        "proxy": "http://"+proxies
    }
    ud =  "http://103.71.69.97:28080/request"
    response = requests.post(ud, json=dt, timeout=timeout, allow_redirects=False)
    return response
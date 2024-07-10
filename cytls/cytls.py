import requests
import json as jn
from urllib.parse import urlencode
import http.cookies
import urllib
ud =  "http://103.71.69.97:28080/request"
def get(url, headers=None, proxies=None, params=None, cookies=None, timeout=40, http2=False, allow_redirects=True):
    if params != None:
        url = url.split("?")[0]
        url = f'{url}?{urlencode(params)}'

    if headers == None:
        headers = {}
    if cookies != None:
        headers["Cookie"] = '; '.join([f'{k}={v}' for k, v in cookies.items()])
    for k,v in headers.items():
        if v == None or v == '':
            headers[k] = ' '

    if proxies == None:
        print("Please bring your proxy IP address!!!")
        return

    if "http" in proxies:
        proxies = proxies['http'].split('/')[-1].strip()
    if "https" in proxies:
        proxies = proxies['https'].split('/')[-1].strip()

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

    response = requests.post(ud, json=dt, timeout=timeout, allow_redirects=False)
    set_cookies = response.headers.get('Set-Cookie')
    if set_cookies:
        cookies = set_cookies.split(', ')
        parsed_cookies = http.cookies.SimpleCookie()

        for cookie in cookies:
            if 'path' in cookie:
                end_pos = cookie.find(';') + 1
                single_cookie_str = cookie[:end_pos].strip()
                parsed_cookies.load(single_cookie_str)
        response.cookies = parsed_cookies

    return response


def post(url, headers=None, proxies=None, params=None, cookies=None, json=None, data=None, timeout=40, http2=False,
         allow_redirects=True):
    if params != None:
        url = url.split("?")[0]
        url = f'{url}?{urlencode(params)}'

    if headers == None:
        headers = {}
    if cookies != None:
        headers["Cookie"] = '; '.join([f'{k}={v}' for k, v in cookies.items()])
    for k,v in headers.items():
        if v == None or v == '':
            headers[k] = ' '

    if type(data) == type({}):
        data = urllib.parse.urlencode(data)

    if proxies == None:
        print("Please bring your proxy IP address!!!")
        return

    if "http" in proxies:
        proxies = proxies['http'].split('/')[-1].strip()
    if "https" in proxies:
        proxies = proxies['https'].split('/')[-1].strip()

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
    response = requests.post(ud, json=dt, timeout=timeout, allow_redirects=False)
    set_cookies = response.headers.get('Set-Cookie')
    if set_cookies:
        cookies = set_cookies.split(', ')
        parsed_cookies = http.cookies.SimpleCookie()

        for cookie in cookies:
            if 'expires' in cookie:
                end_pos = cookie.find(';') + 1
                single_cookie_str = cookie[:end_pos].strip()
                parsed_cookies.load(single_cookie_str)
        response.cookies = parsed_cookies
    return response

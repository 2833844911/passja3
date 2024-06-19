import requests
import json as jn
from urllib.parse import urlencode
 


def get(url, headers=None, proxies=None, params=None,cookies=None, timeout=40, http2=False,allow_redirects=True):
    if params != None:
        url = url.split("?")[0]
        url = f'{url}?{urlencode(params)}'
    
    if headers==None:
        headers = {}
    
    if proxies==None:
        print("Please bring your proxy IP address!!!")
        return
    
    if "http" in proxies:
        proxies = proxies['http'].split('/')[-1].strip()
    if "https" in proxies:
        proxies = proxies['https'].split('/')[-1].strip()
    if cookies != None:
        headers["Cookie"] =  '; '.join([f'{k}={v}' for k, v in cookies.items()])
    if allow_redirects == True:
        cancdx = "0"
    else:
        cancdx = "1"
    dt = {
        "cancdx": cancdx,
        "method": "GET",
        "url": url,
        "headers":headers,
        "postData":"",
        "proxy": proxies,
        "http2": http2
    }
    print(proxies)
    ud = "http://103.71.69.97:7890/request"
    response = requests.post(ud, json=dt,timeout=timeout, allow_redirects=False)
    return response



def post(url, headers=None, proxies=None, params=None,cookies=None,json=None, data = None, timeout=40, http2=False,allow_redirects=True):
    if params != None:
        url = url.split("?")[0]
        url = f'{url}?{urlencode(params)}'
    
    if headers==None:
        headers = {}
    
    if proxies==None:
        print("Please bring your proxy IP address!!!")
        return
    
    if "http" in proxies:
        proxies = proxies['http'].split('/')[-1].strip()
    if "https" in proxies:
        proxies = proxies['https'].split('/')[-1].strip()
    if cookies != None:
        headers["Cookie"] =  '; '.join([f'{k}={v}' for k, v in cookies.items()])
    postData = ""
    if data != None:
        postData = data
    if json != None:
        postData = jn.dumps(json)
        headers['Content-Type'] = 'application/json'

    if allow_redirects == True:
        cancdx = "0"
    else:
        cancdx = "1"
    dt = {
        "cancdx": cancdx,
        "method": "POST",
        "url": url,
        "headers":headers,
        "postData": postData,
        "proxy": proxies
    }
    print(dt)
    ud = "http://103.71.69.97:7890/request"
    response = requests.post(ud, json=dt,timeout=timeout, allow_redirects=False)
    return response





import requests
import json as jn
from urllib.parse import urlencode, urljoin
import urllib
from types import MethodType
import http.cookies

ud =  "http://103.71.69.63:28080/request"

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

    # if allow_redirects == True:
    #     cancdx = "1"
    # else:
    #     cancdx = "0"
    dt = {
        "cancdx": "0",
        "method": "GET",
        "url": url,
        "headers": headers,
        "timeout": timeout,
        "postData": "",
        "proxy": "http://"+proxies,
        "http2": http2
    }

    response = requests.post(ud, json=dt, timeout=timeout, allow_redirects=False)
    response.url = url
    set_cookies = response.headers.get('Set-Cookie')
    if set_cookies:
        parsed_cookies = http.cookies.SimpleCookie()
        # 将 set_cookies 字符串拆分为单个 Cookie
        cookies_list = set_cookies.split(', ')

        # 逐个加载每个 Cookie
        for cookie_str in cookies_list:
            parsed_cookies.load(cookie_str)
        # parsed_cookies.load(set_cookies)
        response.cookies = parsed_cookies
        cookies_dict = {key: morsel.value for key, morsel in response.cookies.items()}
        cookies.update(cookies_dict)
    if allow_redirects == True:
        if response.status_code == 303:
            return get(urljoin(url,response.headers['Location']), headers, proxies, params, cookies, timeout, http2, allow_redirects)
        elif response.status_code == 302:
            return get(urljoin(url,response.headers['Location']), headers, proxies, None, cookies, timeout, http2, allow_redirects)
        elif response.status_code == 301:
            return get(urljoin(url,response.headers['Location']), headers, proxies, None, cookies, timeout, http2, allow_redirects)

    return response


def post(url, headers=None, proxies=None, params=None, cookies=None, json=None, data=None, timeout=40, http2=False,allow_redirects=True):
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

        headers['Content-Type'] = 'application/x-www-form-urlencoded'
    if json != None:
        postData = jn.dumps(json)
        headers['Content-Type'] = 'application/json'

    # if allow_redirects == True:
    #     cancdx = "1"
    # else:
    #     cancdx = "0"
    dt = {
        "cancdx": "0",
        "method": "POST",
        "url": url,
        "headers": headers,
        "postData": postData,
        "timeout": timeout,
        "proxy": "http://"+proxies,
        "http2": http2
    }
    response = requests.post(ud, json=dt, timeout=timeout, allow_redirects=False)
    set_cookies = response.headers.get('Set-Cookie')
    if set_cookies:
        parsed_cookies = http.cookies.SimpleCookie()
        # 将 set_cookies 字符串拆分为单个 Cookie
        cookies_list = set_cookies.split(', ')

        # 逐个加载每个 Cookie
        for cookie_str in cookies_list:
            parsed_cookies.load(cookie_str)

        response.cookies = parsed_cookies
        cookies_dict = {key: morsel.value for key, morsel in response.cookies.items()}
        cookies.update(cookies_dict)
    response.url = url
    if allow_redirects == True:
        if response.status_code == 303:
            return post(urljoin(url,response.headers['Location']),headers, proxies, None, cookies, json, data, timeout, http2,allow_redirects)
        elif response.status_code == 302:
            return get(urljoin(url,response.headers['Location']), headers, proxies, None, cookies, timeout, http2, allow_redirects)
        elif response.status_code == 301:
            return get(urljoin(url,response.headers['Location']), headers, proxies, None, cookies, timeout, http2, allow_redirects)

    return response


class Session:
    def __init__(self):
        self.cookies = {}
        self.s = requests.session()


    def addCookie(self):
        pass

    def get(self,url, headers=None, proxies=None, params=None, cookies=None, timeout=40, http2=False, allow_redirects=True,verify=False):
        if cookies:
            self.cookies.update(cookies)
        response = get(url, headers, proxies, params, self.cookies, timeout, http2, allow_redirects)
        self.cookies.update(response.cookies)
        set_cookies = response.headers.get('Set-Cookie')
        if set_cookies:
            cookies_dict = {key: morsel.value for key, morsel in response.cookies.items()}
            self.cookies.update(cookies_dict)

        parsed_cookies = http.cookies.SimpleCookie()

        # 将字典中的键值对添加到 SimpleCookie 对象中
        for key, value in self.cookies.items():
            parsed_cookies[key] = value
        response.cookies =parsed_cookies

        def get_cookie(self, key, default=None):
            if key in self:
                return self[key].value
            else:
                return default

        # 将新的 get 方法绑定到 response.cookies
        response.cookies.get = MethodType(get_cookie, response.cookies)

        return response


    def post(self,url, headers=None, proxies=None, params=None, cookies=None, json=None, data=None, timeout=40, http2=False,allow_redirects=True,verify=False):
        if cookies:
            self.cookies.update(cookies)
        response = post(url, headers, proxies, params, self.cookies, json, data, timeout, http2,allow_redirects)
        set_cookies = response.headers.get('Set-Cookie')
        if set_cookies:
            cookies_dict = {key: morsel.value for key, morsel in response.cookies.items()}
            self.cookies.update(cookies_dict)
        parsed_cookies = http.cookies.SimpleCookie()

        # 将字典中的键值对添加到 SimpleCookie 对象中
        for key, value in self.cookies.items():
            parsed_cookies[key] = value
        response.cookies =parsed_cookies

        # 定义一个新的 get 方法
        def get_cookie(self, key, default=None):
            if key in self:
                return self[key].value
            else:
                return default

        # 将新的 get 方法绑定到 response.cookies
        response.cookies.get = MethodType(get_cookie, response.cookies)

        return response



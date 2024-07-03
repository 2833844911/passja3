from cytls import cytls

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}


proxies =  {"https": "http://14.121.105.170:8008"}

url ="https://www.baidu.com/"
req = cytls.get(url, headers=headers, proxies=proxies)


dt = req.text
print(req.status_code)
print(req.headers)
print(dt)

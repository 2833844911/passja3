# Perfect TLS forwarding calls break through the JA3 check


Use the same as requests.
The project fully emulates the TLS fingerprint of the browser.

##### Test examples (CloudFlare)

```python
from cytls import cytls

headers = {
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "accept-language": 'en-US,en;q=0.9',
    "upgrade-insecure-requests": "1",
    "sec-ch-ua-mobile": "?0",
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "priority": "u=0, i",
    "sec-ch-ua-platform": '"Windows"',
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br, zstd",
}
proxies = {"https": "http://user:passwd@255.255.255:8888"}

url = "https://www.utmel.com/productdetail/texasinstruments-tps63802dlar-7758755"

req = cytls.get(url, headers=headers, proxies=proxies, allow_redirects=True)


dt = req.text
print(req.status_code)
print(req.headers)
print(dt)


```

outcome

![image-haom.png](./image-haom.png)
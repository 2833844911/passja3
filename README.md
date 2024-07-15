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


Contact email 2833844911@qq.com


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


Contact email 2833844911@qq.com



### cronet Browser Request Library Local Forwarding to Bypass JA3

#### Installing Docker on a CentOS System Can Be Done as Follows:

1. Uninstalling Old Versions of Docker
   
   First, if there are old versions of Docker installed on your system, you need to uninstall them. Older versions might be referred to as docker or docker-engine. Use the following commands to uninstall:   
   
```bash
   sudo yum remove docker \
                   docker-client \
                   docker-client-latest \
                   docker-common \
                   docker-latest \
                   docker-latest-logrotate \
                   docker-logrotate \
                   docker-engine
```
2. Setting Up the Docker Repository
   
   Install necessary packages that will allow yum to use packages from HTTPS sources:
   
   
```bash
   sudo yum install -y yum-utils
```
   
   Next, set up the stable repository:
   
   
```bash
   sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

   sudo yum update -y && sudo yum install -y docker-ce docker-ce-cli containerd.io
```

3. Starting Docker
   
   After installation, start the Docker service:
   
   
```bash
   sudo systemctl start docker
```
4. Download the Image (cytlszf.tar)
   Link：https://pan.baidu.com/s/1NSEr8Q3SxeUNu7vG6jYZ9w
   Access Code：lrck
   OR
   https://drive.google.com/file/d/1apHnsBal4Lzhs8iajqB4ay-DGtHstceO/view?usp=sharing

6. Loading the Image
   
   
```bash
   docker load -i cytlszf.tar
```
6. Starting the Container (Opening Port 28080 on the Server)
   
   
```bash
   docker run -p 28080:8081 -d cytlszf:latest
```
7.Download the passja3 Project
   
   Link: [passja3](https://github.com/2833844911/passja3 "to")
8. Replace the Top Link of cytls.py with Your Own
   Replace
   ud =  "http://103.71.69.97:28080/request"
   with
   ud =  "http://yourip:28080/request"
9. Normal Usage of the passja3 Project

can see
https://github.com/wmm1996528/cronet-go/tree/main/examples

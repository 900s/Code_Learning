import requests
url = "https://x.com/900_later"

# 根据网站协议不同需要使用相应协议代理 (http, https, socks)
dict_proxies = {
    "https": "127.0.0.1:7897"       # 使用clash verge本地全局代理
}

response = requests.get(url, proxies = dict_proxies, timeout = 5)
print(response.status_code)

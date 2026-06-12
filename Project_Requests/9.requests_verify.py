import requests
url = "https://self-signed.badssl.com"

# verify参数能忽略CA证书认证
response = requests.get(url, verify = False)
print(response.status_code)
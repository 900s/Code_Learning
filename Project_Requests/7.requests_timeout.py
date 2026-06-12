import requests
url = "https://x.com/home"

# timeout: 经过设定的秒数时间之后停止等待响应
response = requests.get(url, timeout = 3)
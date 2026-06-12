import requests
url = "https://www.doubao.com/"

response = requests.get(url)
print(len(response.content.decode()))

# 右键检查 -> 刷新 -> 选择网络 -> 选择包 -> 获得User-Agent
# 构建请求头字典
dict_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
}

# 发送带请求头的请求
response1 = requests.get(url, headers = dict_headers)
print(len(response1.content.decode()))
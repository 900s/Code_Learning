import requests
url = "https://search.bilibili.com/all"

dict_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
}

# 构建参数字典
# 关键参数简单获取方法: 一个个删, 直到页面发生改变
dict_params = {
    "keyword": "沫子解说"
}

response = requests.get(url, headers = dict_headers, params = dict_params)
print(response.url)

# 从网络获取响应内容，然后将该内容保存到本地一个名为 bilibili.html 的文件里
# wb: 二进制写入模式
with open("bilibili.html", "wb") as f:
    f.write(response.content)

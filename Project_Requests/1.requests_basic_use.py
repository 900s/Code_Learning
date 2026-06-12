# 安装Requests
# pip install requests (终端输入)

import requests
url = "https://sr.mihoyo.com/main"

response = requests.get(url)
print(response)         # 打印响应对象的状态信息 (200：HTTP 状态码，表示请求成功)
print(response.text, type(response.text))    # 打印服务器返回的网页源码

# response.text = response.content.decode(推测出的编码字符集), 可能会有乱码
# 方法一: 手动设定编码格式
response.encoding = "utf-8"
print(response.text)

# 方法二: response.content (存储bytes类型的源码, 可进行decode操作, 推荐使用)
print(response.content.decode("utf-8"))     # 括号内不填默认为utf-8

# 常见的响应对象参数和方法
# 响应url
print(response.url)

# 响应状态码
print(response.status_code)

# 响应对应的请求头
print(response.request.headers)

# 响应头
print(response.headers)

# 响应的cookie (类型是 RequestsCookieJar)
print(response.cookies, type(response.cookies))


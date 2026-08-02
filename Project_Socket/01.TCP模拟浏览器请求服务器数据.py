import socket

# 创建会话对象
# socket.socket(): 创建一个套接字对象
# socket.AF_INET: 指定地址族，AF_INET 代表使用 IPv4, AF_INET6 代表使用 IPv6
# socket.SOCK_STREAM: 指定套接字类型, SOCK_STREAM 代表使用 TCP 协议, SOCK_DGRAM 对应 UDP 协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接 (内部类型为元组)
# HTTP 网页服务默认端口: 80
# HTTPS 加密网页服务默认端口: 443
sk.connect(("www.baidu.com", 80 ))      # 只需要域名, 不需要 http 等协议前缀

# 数据传输
# 请求行: GET / HTTP/1.1 → 用 GET 方法获取根路径 /，协议版本 1.1
# \r\n: 回车换行，HTTP 协议规定的行分隔符
# Connection: close → 告诉服务器“响应完就断开连接，别保持长连接”
# \r\n\r\n: 表示请求头结束
# 字符串前面加 b 表示这是一个 bytes（字节串）, 因为 Socket 只能发送字节流
request = (
    b"GET / HTTP/1.1\r\n"
    b"Host: www.baidu.com\r\n"
    b"Connection: close\r\n"
    b"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36 Edg/150.0.0.0\r\n"
    b"\r\n"
)
sk.send(request)

# 等待数据
# sk.recv(1024): 从套接字 sk 接收最多 1024 个字节的数据
data_list = []
while True:
    data = sk.recv(1024)
    if data:
        data_list.append(data)
    else:
        break
# 连接符.join(列表): 用连接符把一个列表里的所有元素拼成一个完整的字符串（或字节串）
# 连接符: 拼在每个元素之间的东西。如果是空字符串 ""，就是直接拼接
data_str = (b"".join(data_list)).decode("utf-8")

print(data_str)
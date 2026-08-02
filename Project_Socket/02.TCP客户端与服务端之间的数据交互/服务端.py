import socket

# 创建会话对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接 (服务端用 bind)
# 内网ip在cmd里用ipconfig查
# 端口尽量选用8000及以上, 避免冲突
server.bind(("192.168.247.1", 8080))

# 设置监听
# server.listen(5): 把套接字server设置为监听模式，并设定最多能同时排队等候的连接数为 5 个
server.listen(5)
print("服务端启动成功!")

# 阻塞连接
# info: 一个新的套接字对象，专门用来和这个客户端通信
# addr: 客户端的地址信息，是一个元组 (IP地址, 端口号)
info, addr = server.accept()    # 阻塞等待，直到有客户端连接进来, 一旦有客户端连接，就返回两个值

# 等待数据
while True:
    data = info.recv(1024)
    print(f"收到客户端信息: {data.decode("utf-8")}")
    back_data = input("请输入发给客户端的信息: ")
    info.send(back_data.encode("utf-8"))


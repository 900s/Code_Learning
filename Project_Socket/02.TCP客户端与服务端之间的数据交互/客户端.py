import socket

# 创建会话对象
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接 (客户端用 connect)
client.connect(("192.168.247.1", 8080))

# 发送数据
while True:
    info = input("请输入发给服务端的信息: ")
    client.send(info.encode("utf-8"))
    back_info = client.recv(1024)
    print(f"收到客户端信息: {back_info.decode("utf-8")}")


# 循环案例1: 根据输入的用户名密码执行登录操作
while True:
    ad = input("请输入用户名: ")
    pw = input("请输入密码: ")
    if ad == "" or pw == "":
        print("输入的用户名或密码不能为空!")
        continue        # continue: 表示中断本次循环, 直接进入下一次循环
    if (ad == "admin" and pw == "666888") or (ad == "zhangsan" and pw == "123456") or (ad == "taoge" and pw == "888666"):
        print("登录成功, 进入b站首页")
        break
    else:
        print("用户名或密码错误, 请重新输入!")



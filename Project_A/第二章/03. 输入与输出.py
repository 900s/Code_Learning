# input(提示语) ---> 获取键盘上输入的数据
password = input("请输入取款密码: ")
print(f"密码为{password}, 密码正确。")
money = input("请输入取款金额: ")
print(f"已取款{money}元, 剩余金额为{10000 - int(money)}元。")      # 输入均为str类型, 需转换
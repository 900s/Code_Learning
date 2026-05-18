# 异常处理
try:                            # 可能出现异常的业务代码
    num = int(input("请输入数字:"))
    print(num)
except NameError as e:          # 捕获类型为NameError的异常并取名为e
    print(f"出现错误, 请联系管理员, 错误类型为{e}")
except Exception as e:          # 捕获所有类型异常并取名为e
    print(f"出现错误, 请联系管理员, 错误类型为{e}")
finally:                        # 无论程序是否正常运行, finally代码块中的代码都会运行
    print("释放资源")
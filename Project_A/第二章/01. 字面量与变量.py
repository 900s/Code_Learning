# 字面量的写法
print(100)          # int
print(3.14)         # float
print(True)         # bool
print(False)        # bool
print(None)         # NoneType (空值)
print("Manba Out")  # str (字符串)

# 布尔类型本质也是整数类型 (True = 1, False = 0)
print(True + 1)

# 变量 ---> Python是动态类型语言, 一个变量可以存储不同类型数据 (但是项目开发中, 一个变量推荐只存储一种数据)
base, incr = 100, 50
print("未来第一个月的资金总额为:", base + incr, "万元")
print("未来第二个月的资金总额为:", base + incr*2, "万元")

# 标识符 (只能包含字母, 数字, 下划线)
# 命名规范: 1.见名知意; 2. 多个部分使用下划线连接 (如 first_name); 3. 英文字母全小写
true = 1            # 不能使用关键字,如 True
name6 = 2           # 不能以数字开头
print(true, name6)
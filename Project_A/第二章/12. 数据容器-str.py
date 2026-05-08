## 字符串基本操作 (除无法修改外与列表一致)
s = " Python "
print(s[-1: : -1])              # 字符串步长为负数, 从后往前截取, 起始索引必须大于结束索引

##字符串常用方法
# find(): 查找指定字符串第一次出现的索引位置
print(s.find("o"))

# count(): 统计子字符串在指定字符串中出现的次数
print(s.count("o"))

# upper(): 转为大写
print(s.upper())

# lower(): 转为小写
print(s.lower())

# split(): 将字符串按照指定字符串切割 - 结果为列表
print(s.split("o"))

# strip(): 去除字符串两端的空格或指定字符
print(s.strip())

# replace(): 将字符串中的指定子串替换为新的内容
print(s.replace("Python", "Java"))

# startswith() / endswith(): 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print("Python是以P开头的吗?", s.startswith(" P"))
print("Python是以P结尾的吗?", s.endswith("P"))

# 案例1: 邮箱格式验证 (只能包括一个@, 至少包括一个.)
# 方式一: 传统方法
mail = input("请输入邮箱地址: ")
if mail.count("@") == 1 and mail.count(".") >= 1:
    print("该邮箱地址合法")
else:
    print("该邮箱地址不合法")
# 方式二: in运算符 ---> 判断子串是否在字符串中
if mail.count("@") == 1 and "." in mail:
    print("该邮箱地址合法")
else:
    print("该邮箱地址不合法")

# 案例2: 判断字符串是否是回文
s1 = input("请输入字符串: ")
s2 = s1[ : : -1]
i = 0
while s1[i] == s2[i]:
    i += 1
    if i > len(s1) - 1:
        print("该字符串是回文")
        break
else:
    print("该字符串不是回文")


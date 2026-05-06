# type(数据) ---> 获取指定字面量或变量类型
name = "Kobe"
print(name, type(name))

# isinstance(数据, 类型) ---> 判断数据是否是指定类型
print(isinstance(name, str))

# 定义字符串的三种方式
s1 = "str"
s2 = 'str'
s3 = '''
        s
        t
        r'''
print(s1)
print(s2)
print(s3)

# 转义字符 (\', \", \n, \t(增加缩进, 缩进一个tab大小))
s2 = '\t It\'s my name.'
print(s2)

# 字符串拼接与格式化
age = 47
pro = "篮球运动员"
say = "Man, hahahaha, what can I say, Manba out."
print("孩子们好, 我是" + name + ", 今年" + str(age) + "岁了, 我是一名" + pro + ", 令孩子们印象深刻的一句话想必是: \"" + say + "\"")
# 用"+"拼接字符串不能与非字符串拼接
print("孩子们好, 我是%s, 今年%s岁了, 我是一名%s, 令孩子们印象深刻的一句话想必是: \"%s\"" %(name, age, pro, say))
print(f"孩子们好, 我是{name}, 今年{age}岁了, 我是一名{pro}, 令孩子们印象深刻的一句话想必是: \"{say}\"")
# 推荐用f






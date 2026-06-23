import re
# 重复符{}: 指定左边字符或字符集可以重复的数量范围
s = "employee apple age aPe anxiety a@e a#e a\ne alpha acquire anxious a5e a9e"
list1 = re.findall("a[a-z]{1,3}e", s)       # 通配符.重复1~3次
list2 = re.findall("e.{5,6}e", s)
print(list1)
print(list2)        # 默认贪婪匹配 (同一字符串按最大匹配数进行匹配)
# 在重复符后加?可以取消贪婪匹配, 即同一字符串按最小匹配数进行匹配
list3 = re.findall("e.{5,6}?e", s)
print(list3)
list4 = re.findall("e.{5,}e", s)        # 通配符.重复5~+∞次
print(list4)        # 不匹配\n所以列表有两项
list5 = re.findall("a.{5,}e", s, re.S)  # 更改匹配模式, 可以匹配任意字符
print(list5)
import re

# Python内置查询, 返回索引位置
s = "man sajdoiawjdowjma"
print(s.find("man"))

# 正则查询, 返回列表
s = "yugan 123 manba 456"
list = re.findall(r"\d+", s)        # r"...": 原始字符串，不转义反斜杠
print(list)

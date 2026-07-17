import re

with open("error.log") as f:
    text = f.read()

# 查询所有error
list1 = re.findall("ERROR:.*", text)
print(list1)

# re.search: 查询第一个匹配对象并返回match对象, 否则返回None
# 查询第一个error
list2 = re.search("ERROR:.*", text)
print(list2)
print(list2.span())
print(list2.start())
print(list2.end())
print(list2.group())    # list.group(): 提取整体组内容, 括号内可填组名具体查询

# 有名分组
# 匹配第一个备用服务器地址
memo = '''
服务器的 IP 地址如下：
主服务器：192.168.1.1
备用服务器：10.0.0.5
外部服务器：172.16.254.1
无效 IP：256.100.50.25 和 192.168.1.256
'''
# (?P<name>content): 给组起名字, 便于提取组内容
list3 = re.search(r"\b备用服务器：(?P<backup_ip>(?:\d{1,3}\.){3}\d{1,3})\b", memo)
print(list3)
print(list3.group("backup_ip"))

# re.match: 相当于re.search("^text", string)
# re.split: 对字符串进行正则分割
# re.sub: 选择文本匹配替换
s = "Piggod   I will  kill   you !"
list4 = re.split(r"\s+", s)
list5 = re.sub(r"\s+", " ", s)
print(list4)
print(list5)

# re.compile: 类似于定义函数用于重复使用
log = "18983771690, awkward, 1098015460@qq.com, genshin impact, 4399, +8613981820845"
reg = re.compile(r"(?:\+86)?1[3-9]\d{9}\b")
list6 = reg.findall(log)
print(list6)



import re

s1 = "employee apple age a_e aPe anxiety alpha acquire anxious a5e a9e"
# 避免因解析出现警告, 可写为\\d 或者 r"\d", 所有 \ 不再被解析成转义字符
# f""用于在字符串里嵌入变量, 可与r组合使用, 不区分先后, 如rf""
ret1 = re.findall("\\d+", s1)     # \d: 匹配一个数字原子. 等价于[0-9]
ret2 = re.findall(r"\w+", s1)     # \w: 匹配一个单词原子. 等价于[0-9a-zA-Z_]
# \D: 等价于[^0-9]
# \W: 等价于[^0-9a-zA-Z_]
# \s: 匹配一个任意空白字符原子, 比如空格
# \S: 匹配一个任意非空白字符原子
# \b: 匹配一个单词边界原子 (不会匹配有边界之外的)
# 单词边界可以理解为单词字符和非单词字符之间的那个“缝隙”
s2 = "鱼干 鱼干卡比兽 煤炭龟鱼干"
ret3 = re.findall(r"\b鱼干\b",s2)

s3 = "*** **** *****"
ret4 = re.findall(r"\*+",s3)

s4 = r"E:\Game\表情包—哥伦比娅&桑多涅\哥伦比娅\哥伦比娅.png"
ret5 = re.findall(r"E:\\Game\\表情包—哥伦比娅&桑多涅\\哥伦比娅\\哥伦比娅\.png",s4)
# r让 \ 不再被解析成Python转义字符, \\ 让 \ 不再被解析成正则转义字符

print(ret1)
print(ret2)
print(ret3)
print(ret4)
print(ret5)


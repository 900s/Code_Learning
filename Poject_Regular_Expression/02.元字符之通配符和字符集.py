import re
# 通配符.: 匹配1个除了换行符\n以外任何字符
s = "apple ape alpha acquire anxious a\ne"
ape = re.findall("a.e", s)
print(ape)
apple = re.findall("a...e", s)
print(apple)

# 字符集[]: 匹配1个[]内的字符, []内各字符间无需逗号
s = "apple age aPe anxiety a@e a#e alpha acquire anxious a5e a9e"
alpha = re.findall("a[a-zA-Z5]e", s)
print(alpha)
number = re.findall("a[0-9]e", s)
print(number)
reverse = re.findall("a[^0-9a-zA-Z]e", s)     # ^: 取反, 除了[]内的字符均匹配
print(reverse)


import re

# ^: 开始边界符, 匹配一行开头位置
# $: 结束边界符. 匹配一行结束位置
path = "http://github.com/900s/Code_Learning/"
reg = r"^https?://github\.com/[a-zA-Z0-9_]+/[a-zA-Z0-9_]+/$"    # 在 . 前加 \ 避免 . 被识别为通配符
ret = re.findall(reg, path)
print(ret)
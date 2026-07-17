import re

text = """
Visit us at user@qq.com for more info.
Contact support at support@qq.com.
Also, check out admin@shturl.cc and info@163.com
"""
ret1 = re.findall(r"\b([\w.-]+)@\b", text)   # (): 优先提取其中的内容
print(ret1)

ret2 = re.findall(r"\b[\w.-]+@\w+\.(?:cc|com)\b", text)     # 在()内首先加?:取消优先提取
print(ret2)
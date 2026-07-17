import re
import requests

s = "employee apple age ae aPe anxiety a@e a#e a\ne alpha acquire anxious a5e a9e"

list1 = re.findall("e.*e", s)           # *等同于{0,}
print(list1)

url = "https://www.baidu.com/"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}
response = requests.get(url, headers = headers)
list2 = re.findall('"title-content-title">(.*?)</span>', response.text)
for i in list2:
    print(i)

# 在重复符后加?可以取消贪婪匹配, 即同一字符串从左往右按最小匹配数进行匹配
list3 = re.findall("a.+?e", s)           # +等同于{1,}
print(list3)


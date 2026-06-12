import requests
url = "https://www.baidu.com/"

response = requests.get(url)

dict_cookies = requests.utils.dict_from_cookiejar(response.cookies) # 把 CookieJar 转成字典
print(dict_cookies)
jar_cookies = requests.utils.cookiejar_from_dict(dict_cookies)      # 把字典转回 CookieJar
print(jar_cookies)
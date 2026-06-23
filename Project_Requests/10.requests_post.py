import requests
import json
import sys

"""
post 数据来源:
1. 固定值
2. 输入值
3. 预设值 - 静态文件 (已提前生成, 直接从静态html中获取)
4. 预设值 - 发送请求 (需要对指定地址发送请求获取)
5. 客户端生成
"""

class Translation:
    def __init__(self):
        self.url = "https://api.interpreter.caiyunai.com/v1/translator"
        self.url1 = "https://api.interpreter.caiyunai.com/v1/user/jwt/generate"
        self.headers = {
            # 在请求标头中获取
            # authorization, x-authorization可能有过期时间, 需要手动更新
            "authorization": "Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6Inh5ODZhNWFlIiwidHlwIjoiSldUIn0.eyJhdWQiOlsieGlhb3lpIl0sImV4cCI6MTc4MTgzNTgyMSwiaWF0IjoxNzgxNTc2NjIxLCJkZXZpY2VfaWQiOiIwM2ZjNGNjN2FmNTI5Yzc1ZDc3MTEwMmFiNmRkNTNiZSIsInVzZXJfdHlwZSI6MywidmVyc2lvbiI6M30.v-6ON4l9DQR4-NwpKiZId8edvl2JiLZH05huHGu0YFhjtW2gokFpVeyLYYnB2ThaewHOykBmJ6hU9i5UQ5m2BQ",
            "origin": "https://fanyi.caiyunapp.com",
            "os-type": "web",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
            "version": "4.7.0",
            "x-authorization": "token:qgemv4jr1y38jyq6vhvi"
        }

    def get_browser_id(self):
        """
        获得用于认证的浏览器id
        :return: 浏览器id
        """
        browser_data = requests.post(self.url1, headers = self.headers)
        # 通过json库的loads函数将json字符串转换成python字典
        dict_browser_data = json.loads(browser_data.content)
        return dict_browser_data["jwt"]

    def run(self):
        """
        进行翻译操作得到结果并解码
        """
        self.headers["t-authorization"] = self.get_browser_id()
        # content-type: application/json 表明服务器接收json类型数据
        # requests 库的json参数会自动把你的字典转成json字符串
        response = requests.post(self.url, json = self.data(), headers = self.headers, timeout = 1)
        response.encoding = "utf-8"
        dict_response = json.loads(response.content)
        parse_data = dict_response["target"][0]
        print(f"翻译结果为：{parse_data}")       # 未知加密处理, 因此是乱码

    def data(self):
        """
        输入需要翻译的文本
        :return: post所需的data字典
        """
        dict_data = {
            # 在响应中获取
            # browser_id 一般不会变化(除非手动清除浏览器缓存或重装系统)
            "browser_id": "03fc4cc7af529c75d771102ab6dd53be",
            "detect": "true",
            "source": [word, ""],
            "trans_type": "auto2en"
        }
        return dict_data

if __name__ == "__main__":
    word = input("请输入想翻译的中文: ")
    # word = sys.argv[1]: 另一种运行方式, 需要sys库, 终端内使用, 格式为 python3 10.requests_post.py 想翻译的中文
    caiyun = Translation()
    caiyun.run()



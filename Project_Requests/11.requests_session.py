# requests.session: 自动处理cookie, 用于连续的多次请求
import requests
import re

def login():
    """
    获取token并保持登录状态
    """
    # 创建session实例
    session = requests.session()
    # 可直接在session里加headers
    session.headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
    }
    url1 = "https://github.com/login?return_to=https%3A%2F%2Fgithub.com%2Fdashboard"
    # 正则表达式只能在字符串上使用, 所以要先转化
    response1 = session.get(url1).content.decode("utf-8")
    # 如果字符串里包含双引号，外面就用单引号包
    # 如果字符串里包含单引号，外面就用双引号包
    # 如果需要同时包含单引号和双引号，用三引号包
    # re.findall(要匹配的内容, 被搜索的字符串): 在字符串里找到所有匹配的内容，返回一个列表
    # (): 捕获组，把括号里匹配到的内容单独返回
    # .: 匹配任意单个字符（除换行符外）
    # *: 匹配多次
    # ?: 非贪婪模式，尽可能少地匹配
    token = re.findall('name="authenticity_token" value="(.*?)"', response1)

    url2 = "https://github.com/session"
    dict_data = {
        "commit": "Sign in",
        "authenticity_token": token,
        "login": "1098015460@qq.com",
        "password": "wyx20010905@"
    }
    response2 = session.post(url2, data = dict_data)
    if response2.status_code == 200:
        print("登录成功")

    url3 = "https://github.com/900s"
    response3 = session.get(url3)
    name_list = re.findall("<title>(.*?)</title>", response3.text)
    for i in name_list:
        if i == "900s":
            print("验证登录成功")
            return
    print("验证登录失败, 请检查代码")

if __name__ == "__main__":
    login()


import requests
url = "https://github.com/900s"

dict_headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0",
}
temp = "_octo=GH1.1.1076202565.1761922719; _device_id=6c2e21dc163ab8491b35ce4910eedad3; saved_user_sessions=99709702%3AOyDMjqK-5i034YvZI7tySNx5__u1j5kUaTT0Iz7psYins8-f; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; user_session=OyDMjqK-5i034YvZI7tySNx5__u1j5kUaTT0Iz7psYins8-f; __Host-user_session_same_site=OyDMjqK-5i034YvZI7tySNx5__u1j5kUaTT0Iz7psYins8-f; tz=Asia%2FShanghai; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=yes; dotcom_user=900s; last_write_ms=1781233546307; _gh_sess=5w9zCCxJLmUtHu742FFq4pMOtCV%2FBRTNHLTPv7YtFPEIP0VuOKclkt%2FAt5A4GXPAe%2B5G9WChGidujwJjFdFN8TeOM27Aul5btbZ4qmhWaOr%2Fd8SJlz%2F2d8vlCcxV6bMV0vABGYXwfF0KJB5uMmuIY2jjGFfPgEKUI8Fg2LXx2eHQqDeoSB%2BUDps8KkJQ6dF8yrwnPsuxv%2FT9EhPFLdAgvScV6N60uuEqUtrV4CrWEpo5Jy8qFsp%2Fs%2FOWoao6x6lI6WNqubo7LJKd3UgaZVqz5J3kK42JIxyWvDcPlqlCHugg32JHEu2fTg4gw96z9oMSgT4pYoZERfA7ovmhV6k3Go%2FoQ876ZlfKOIMlZcbQjlBYEUmWsC%2B68UCC9NL5NT1mW4MRs54%2BjnFbhxNJfe%2BlPkVi1BTwBd3%2FO92WYMv2NunLh5bpc1fmDeJM2X5OFX%2BujvtXv9E%2FuiaeVfmN0kbDb4TuF83DRaes%2Behn5kF0djs8vGgcc%2BORYnHm3IznHS13GXLwTRauh8UHNs8AyjgprpHGAOqfpWGw5lFB8rE7ZpWh38x4RPrYfjjkSSDnMYMKpV1vi7OHRME3fNllSKSsTjvbiJfC30SvWDjfi%2Bl0VOszHCbc0Xs%2BorRyFy97bZE%2F63pRel7%2FGYxZg95EGI8GgDgReNeddGxLj0BkkDf47W5SHM8Gi%2BIIBV2r1bq0jDMqRrgO6refaCs%3D--UY6vknJb78of%2FzFZ--9TnsAVdTpb28C4WiSXDqQQ%3D%3D"

# 方法一
cookie_list = temp.split(";")
dict_cookies = {}
for cookie in cookie_list:
    dict_cookies[cookie.split("=")[0]] = cookie.split("=")[1]

# 方法二: 字典推导式 ---> 语法格式: {要输入的键: 要输入的值 for i in 序列/列表 if 条件}
dict_cookies = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in cookie_list}

response = requests.get(url, headers = dict_headers, cookies = dict_cookies)
with open("github_with_cookies_1.html", "wb") as f:
    f.write(response.content)



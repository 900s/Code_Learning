# if条件判断: 如果分数超过450, 我就去读清华
score = int(input("请输入你的考研分数: "))
if score > 450:
    print("去读清华!")
else:
    print("不读清华")

# 需求: 根据用户输入的年份, 判断这一年是闰年还是平年
year = int(input("请输入年份: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("该年是闰年")
else:
    print("该年是平年")

# if...elif...else 案例: 判断三角形
a = int(input("请输入三角形第一条边边长: "))
b = int(input("请输入三角形第二条边边长: "))
c = int(input("请输入三角形第三条边边长: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("该三角形为等边三角形")
    elif a == b or b == c or c == a:
        print("该三角形为等腰三角形")
    else:
        print("该三角形为普通三角形")
else:
    print("无法构成三角形")



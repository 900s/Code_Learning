# 案例2: 猜数字游戏
import random
ans = random.randint(1, 100)        # 生成随机数
while True:
    num = input("请输入你猜的数字: ")
    if num == "":
        print("输入无效, 请重新输入!")
        continue
    if int(num) > ans:
        print("你猜的数字比答案大")
    elif int(num) < ans:
        print("你猜的数字比答案小")
    else:
        print("恭喜你猜对了!")
        break
print("答案为", ans)



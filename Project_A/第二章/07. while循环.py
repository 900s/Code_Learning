# while循环: 打印5遍: "人生苦短,我用Python"
i = 0
while i < 5:
    print("人生苦短,我用Python")
    i += 1
else:
    print("打印结束")

# 案例: 计算1~100之间所有偶数累加之和
i = 0
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
else:
    print(f"1~100之间所有偶数累加之和为{sum}")
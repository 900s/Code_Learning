# for循环: 遍历输入的字符串
msg = input("请输入信息: ")
for s in msg:                       # s表示遍历出来的元素 (也可以取其他名称)
    print(f"元素: {s}")
else:
    print("遍历结束")

# 案例: 计算1~100之间所有的奇数之和
total = 0
for number in range(1, 101):        # 获取一个从1开始, 到101结束的数字序列 (不包含101)
    if number % 2 == 1:
        total += number
print("1~100之间所有的奇数之和是", total)
# 或者
total = 0
for number in range(1, 101, 2):     # 获取一个从1开始, 到101结束的数字序列 (不包含101), 步长为2
        total += number
print("1~100之间所有的奇数之和是", total)
# 补充: range(end) 用于获取一个从0开始, 到end结束的数字序列 (不包含end)

# 循环嵌套: 根据输入的长m, 宽n, 用*打印一个长方形
m = int(input("请输入长方形的长: "))
n = int(input("请输入长方形的宽: "))
i = 0
for width in range(n):
    for length in range(m):
        print("*", end = " ")       # end表示每一次输出以什么结束, 默认为\n, 表示换行
    print()

# 嵌套循环案例: 打印九九乘法表
for j in range(1, 10):
    for k in range(1, j + 1):
        print(f"{k} * {j} = {j * k}", end = "\t")
    print()


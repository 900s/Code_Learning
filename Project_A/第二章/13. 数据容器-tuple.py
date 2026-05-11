# 元组基本操作 - tuple ---> 元组不可修改
t1 = (2, 2, 3, 2, 1)                     # 组包, 不加括号也ok

# 切片 (与字符串相同)
print(t1[::-1])

# index() 获取元素的索引 (第一个元素的位置)
print(t1.index(2))

# 注意: 如果定义单元素元组, 单个元素之后需要加上逗号
t2 = (100, )
print(type(t2))

# 解包
a, b, c, d ,e = t1                       # 基础解包: 变量数量与容器元素个数一致
print(a, b, c, d)

a, *b, c, d = t1                         # 扩展解包: * 收集剩余所有元素, 封装到list中
print(a, b, c, d)

# 案例: 快速交换数据
a = 100
b = 200
c = 300
a, b, c = c, b, a
print(a, b, c)
print()

# 案例: 根据提供的学生成绩单, 完成以下需求:
# 计算每个学生的总分, 各科平均分, 然后一并输出出来
# 方式一: 传统方式
student = (
("S001", "王建林", 85, 92, 78),
("S002", "李维", 92, 88, 95),
("S003", "余干", 78, 85, 82)
)
print("学号", "\t姓名", "\t语文", "\t数学", "\t英语", "\t总分", "\t平均分")
for s in student:
    total = s[2] + s[3] + s[4]
    ave = total / 3
    print(f"{s[0]} \t{s[1]} \t{s[2]} \t\t{s[3]} \t\t{s[4]} \t\t{total} \t{ave:.1f}")  # :.1f意思是保留一位小数
print()
# 方式二: 元组解包
print("学号", "\t姓名", "\t语文", "\t数学", "\t英语", "\t总分", "\t平均分")
for number, name, chinese, math, english in student:
    total = chinese + math + english
    ave = total / 3
    print(f"{number} \t{name} \t{chinese} \t\t{math} \t\t{english} \t\t{total} \t{ave:.1f}")
# 统计各科最低分, 最高分, 平均分并输出
chinese_score = [s[2] for s in student]     # 获取各科的成绩列表 (后续才能用列表专用语法)
math_score = [s[3] for s in student]
english_score = [s[4] for s in student]
print(f"""
语文最低分: {min(chinese_score)}, 最高分: {max(chinese_score)}, 平均分:{sum(chinese_score) / len(chinese_score)}
数学最低分: {min(math_score)}, 最高分: {max(math_score)}, 平均分:{sum(math_score) / len(math_score):.1f}
英语最低分: {min(english_score)}, 最高分: {max(english_score)}, 平均分:{sum(english_score) / len(english_score)}
""")
# 查找成绩优秀 (均分大于90) 的学生并输出
for number, name, chinese, math, english in student:
    total = chinese + math + english
    ave = total / 3
    if ave > 90:
        print(f"{name}是优秀学生, 学号为{number}, 均分为{ave:.1f}")




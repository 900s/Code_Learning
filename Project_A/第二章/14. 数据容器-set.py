# 集合 set (无序, 自动去重)
# 定义集合和空集合
s1 = {1, 2, 3, 4}
s2 = set()                      # 空集合定义不可使用{}, {}表示空字典

# 常见方法
# add(): 添加元素到集合
s1.add(5)
print(s1)

# remove(): 移除集合中的指定元素
s1.remove(5)
print(s1)

# pop(): 随机删除集合中的元素并返回
e = s1.pop()
print(e)
print(s1)

# clear(): 清空集合
s1.clear()
print(s1)

# difference(): 求两个集合的差集 (存在于第一个集合但不存在于第二个)
s2 = {1, 2, 3, 4}
s3 = {3, 4, 5, 6}
print(s2.difference(s3))

# union(): 求两个集合的并集
print(s2.union(s3))

# intersection(): 求两个集合的交集
print(s2.intersection(s3))
print()

# 案例
football_set = {"李维", "余干", "丁加兰", "梅西"}
basketball_set = {"李维", "科比", "詹姆斯", "余干"}
art_set = {"丁加兰", "李维", "梵高", "毕加索"}
# 1. 找出同时选修艺术和足球的学生
# 方法一
print(f"同时选修艺术和足球的学生有: {football_set.intersection(art_set)}")
# 方法二: & ---> 交集
print(f"同时选修艺术和足球的学生有: {football_set & art_set}")
print()
# 2. 找出同时选修三门课的学生
print(f"同时选修三门课的学生有: {basketball_set.intersection(football_set).intersection(art_set)}")
print()
# 3. 找出选修了足球, 但没有选修篮球的学生
# 方法一:
print(f"选修了足球, 但没有选修篮球的学生有: {football_set.difference(basketball_set)}")
# 方法二: - ---> 差集
print(f"选修了足球, 但没有选修篮球的学生有: {football_set - basketball_set}")
# 方法三: 集合推导式
s1 = {s for s in football_set if s not in basketball_set}
print(f"选修了足球, 但没有选修篮球的学生有: {s1}")
print()
# 4. 统计每个学生选修的课程数量
class_total = [*football_set, *basketball_set, *art_set]    # 集合也可解包
student_total = football_set | basketball_set | art_set     # | ---> 并集
for s in student_total:
    number = class_total.count(s)
    print(f"{s}选修的课程数量为{number}")

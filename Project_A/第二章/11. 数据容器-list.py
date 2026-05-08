## 列表基本操作
# 定义列表
s = [1, 2.1, True, "man", None]
print(type(s))

# 访问列表元素
print(s[4])                     # 正向索引, 从0开始
print(s[-1])                    # 反向索引, 从-1开始

# 修改
s[3] = "out"
print(s[3])

# 删除del
del s[2::2]
print(s)

# 遍历
for i in s:
    print(i, end=" ")
print()

# 列表list切片 [开始索引: 结束索引: 步长] (不包含结束索引)
print(s[: : 2])                    # 正向索引与反向索引可混用, 均可省略 (默认开始索引为0, 结束索引为列表长度, 步长为1)

## 列表常用方法
# append(): 在列表尾部追加元素
s.append(1.5)
print(s)

# insert(索引, 元素): 在指定索引之前, 插入元素
s.insert(0, 5)
print(s)

# remove(): 移除列表中第一个匹配到的元素
s.remove(1)
print(s)

# pop(): 删除列表中指定索引位置的元素并返回 (如果未指定,默认删除最后一个)
s.pop(0)
print(s)

# sort(): 排序 (升序)
alp = ["A", "B", "D", "C", "E", "F", "G"]
alp.sort()
print(alp)

# reverse(): 反转列表元素
alp.reverse()
print(alp)

# 案例1: 将用户输入的5个数字, 存储到列表中并排序, 输出最值和平均值
num = []
for m in range(5):
    u = int(input("请输入数据: "))
    num.append(u)
num.sort()
print("输入数据:", num, ", 最小值为", min(num), ", 最大值为", max(num), ", 平均值为", sum(num) / len(num))
# min() 和 max(): 获取最值
# sum(): 求和
# len(): 获取元素的个数(列表长度)

# 案例2: 合并两个列表的元素并去重
list1 = [2, 2, 4, 5, 6]
list2 = [5, 6, 7, 8, 9]
list3 = [*list1, *list2]         # 解包: 将列表这一类容器解开成一个个独立的元素
new_list = []
for num in list3:
    if num not in new_list:      # 用in运算符判断元素是否存在于列表中
        new_list.append(num)
print("去重前的列表为:", list3)
print("去重后的列表为: ", new_list)

# 案例3: 生成1~20的平方列表
# 方式一: 传统方式
list1 = []
for num in range(1, 21):
    list1.append(num ** 2)
print(list1)
# 方式二: 列表推导式 ---> 按一定的规则快速生成列表 ---> 语法格式: [要输入的值 for i in 序列/列表 if 条件]
list2 = [i ** 2 for i in range(1, 21)]
print(list2)

# 案例4: 从一个列表中提取所有偶数, 并计算其平方, 组成一个新的列表
num_list = [2, 5, 6, 7, 10, 15]
new_list = [i ** 2 for i in num_list if i % 2 == 0]
print(new_list)




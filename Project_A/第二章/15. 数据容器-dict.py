# 字典 ---> key不能重复 (如果重复, 后面的值会覆盖前面的值), key必须是不可变类型 (str, int, float, tuple)
# 字典无索引下标
# 定义空字典
dict1 = {}
dict2 = dict()

# 常见操作
# 添加 - key不存在就是添加
dict3 = {"李维": 280, "翼翔": 302}
dict3["车金刚"] = 400
print(dict3)

# 修改 - key存在就是修改
dict3["车金刚"] = 100
print(dict3)

# 查询
print(dict3["李维"], dict3.get("李维"))     # 两种方式括号不同 (带.的语法是圆括号)
print(dict3.keys())                         # 获取所有的key
print(dict3.values())                       # 获取所有的value
print(dict3.items())                        # 获取所有的键值对 (以上三种均封装到列表)

# 删除
score = dict3.pop("车金刚")                 # 删除并返回key对应value
print(score)
print(dict3)

del dict3["李维"]                           # 直接删除对应键值对
print(dict3)

# 遍历
for s in dict3.keys():
    print(f"姓名: {s}, 分数: {dict3[s]}")

for s in dict3.items():
    print(f"姓名: {s[0]}, 分数: {s[1]}")

# 案例: 开发一个购物车系统
shopping_cart = {}
system = '''
欢迎使用购物车管理系统!

######## 购物车系统 ########
#       1. 添加购物车      #
#       2. 修改购物车      #
#       3. 删除购物车      #
#       4. 查询购物车      #
#       5. 退出购物车      #
############################
'''
while True:
    print(system)
    operation = input("请选择要执行的操作(1 - 5): ")
    match operation:
        case "1":
            name = input("请输入您想添加的商品名称: ")
            price = float(input("请输入该商品的价格: "))
            num = int(input("请输入想添加的该商品数量: "))
            if name in shopping_cart.keys() and shopping_cart[name]["价格"] == price:     # 字典内嵌套字典可用多[]获取
                shopping_cart[name]["数量"] += num
                print("添加成功!")
            elif name not in shopping_cart.keys():
                shopping_cart[name] = {"价格": price, "数量": num}
                print("添加成功!")
            else:
                print("添加失败, 前后价格不一致, 请重新操作!")
                continue
            print(f"目前购物车情况为: {shopping_cart}")
        case "2":
            name = input("请输入您想修改的商品名称: ")
            if name not in shopping_cart.keys():
                print("该商品不存在于购物车内, 修改失败, 请重新操作!")
                continue
            price = float(input("请输入该商品最新的价格: "))
            num = int(input("请输入该商品在购物车内的数量: "))
            shopping_cart[name] = {"价格": price, "数量": num}
            print("修改成功!")
            print(f"目前购物车情况为: {shopping_cart}")
        case "3":
            name = input("请输入您想删除的商品名称: ")
            if name in shopping_cart:
                del shopping_cart[name]
                print("删除成功!")
            else:
                print("该商品不存在于购物车内, 删除失败, 请重新操作!")
                continue
            print(f"目前购物车情况为: {shopping_cart}")
        case "4":
            name = input("请输入您想查询的商品名称: ")
            if name in shopping_cart:
                print(f"该商品名称为: {name}, 价格为: {shopping_cart[name]["价格"]}, 购物车内数量为: {shopping_cart[name]["数量"]}")
            else:
                print("该商品不存在于购物车内, 查询失败, 请重新操作!")
        case "5":
            print("感谢您的使用, 欢迎下次光临!")
            break
        case _:
            print("操作无效, 请重新操作!")











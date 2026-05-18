# 函数作为参数
def divide(a,b):
    return round(a/b, 2)

def calcu(x, y, oper):
    result = oper(x, y)
    return result

print(calcu(1,3, divide))

# 匿名函数 ---> 格式为 lambda 参数 : 函数体 (只能单行, 返回结果无需return)
data_list = ["Another", "Both", "Count", "David", "Manba", "Genshin"]
data_list.sort(key = lambda item : len(item))                   # sort(key) 表示依据key对列表里每个元素进行升序排序
print(data_list)

# 递归调用案例: 计算n的阶乘
def factorial(n):
    if n != 1:
        return n * factorial(n-1)
    else:
        return 1

print(factorial(10))

"""
案例：定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
具体规则如下：
1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
2. 积分抵扣需要商品金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def shopping(*args, coupon = 0, points = 0, express = 0):  # *args的内容输完后, 后续参数只能用关键字参数
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）, 如 (篮球, 1, 40)
    :param coupon: 优惠券金额
    :param points: 积分数量
    :param express: 运费
    :return: 订单总金额
    """
    price = sum([item[1] * item[2] for item in args])
    if coupon <= price and price > 5000:
        price -= coupon
    if points // 100 < price and price > 5000:
        price -= points // 100
    return price + express

print(shopping(("笔", 2, 200), ("运动饮料", 4, 200), ("打印机", 5000, 1), coupon = 1500, points = 6000, express = 50))
print(shopping(("笔", 2, 400), ("运动饮料", 4, 100), ("打印机", 5000, 1), express = 10))



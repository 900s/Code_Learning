# 注意: 函数定义的时候并不会执行, 只有在调用函数的时候, 函数体的逻辑才会执行
# 函数必须先定义, 后调用
def rectangle_area(l, w):
    area = l * w
    return area

area = rectangle_area(6, 5)
print(area)

# 如果返回值有多个, 多个返回值之间逗号分隔
def circle_area_length(r):
    """
    根据圆的半径, 计算圆的面积和周长
    :param r: 圆的半径
    :return: 圆的面积, 圆的周长
    """                                                 # 函数说明文档, 便于理解和维护
    return 3.14 * r ** 2, round(3.14 * 2 * r, 1)        # round(数值, 保留几位小数)

al = circle_area_length(4)
print(f"{al[0]}, {al[1]}")                              # 多个返回值封装到元组中
help(circle_area_length)                                # help(): 查看函数说明文档, 函数后不加括号






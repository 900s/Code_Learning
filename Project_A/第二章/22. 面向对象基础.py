"""
# 定义类 (命名规范: 每个单词首字母大写, 单词之间无间隔符)
class Car:
    pass

# 创建对象
c1 = Car()

# 动态地为对象添加属性
c1.name = "X5"
c1.color = "white"
c1.brand = "BMW"
c1.price = 500000

# 不推荐
"""
# 定义类
class Car:
    # 类属性 (所有实例对象共享)
    wheel = 4
    tax_rate = 0.1

    # __init__方法是初始化的方法, 会在创建对象时自动调用, 可在该方法中为对象设置相应的属性
    # self: 是第一个参数, 表示当前所创造出来的实例对象
    def __init__(self, name, color, price, brand):
    # 实例属性
        self.name = name
        self.color = color
        self.price = price
        self.brand = brand
        print("Car 类型对象初始化完毕, 对象属性添加完毕")

    # 定义实例方法
    def running(self):
        print(f"{self.brand}{self.name}正在高速行驶中")
    def total_price(self, discount, rate):
        """
        计算提车总费用
        :param discount: 折扣
        :param rate: 税率
        :return: 提车总费用
        """
        total_cost = self.price * (rate + discount)
        return total_cost

    # 定义魔法方法
    def __str__(self):
        return f"{self.name}, {self.color}, {self.price}, {self.brand}"
    def __eq__(self, other):
        return self.name == other.name and self.color == other.color and self.price == other.price and self.brand == other.brand
    def __lt__(self, other):
        return self.price < other.price
    """
    __init__: 初始化方法
    __str__: 字符串表示的方法
    __eq__: 比较两个对象是否相等
    __lt__, __le__, __ge__, __gt__: 小于, 小于等于, 大于, 大于等于
    """


# 创建对象
c1 = Car("X5", "white", 500000, "BMW")
print(c1.__dict__)                                                          # 将对象中所有属性以字典形式输出
print(c1)
c1.running()
print(f"{c1.total_price(0.9, 0.05):.0f}")
print()

c2 = Car("X5", "white", 500000, "BMW")
print(c2 == c1)
print(c2 > c1)                                                               # 虽然定义的lt, 但是大于也能用
print(c2.tax_rate)                           # 通过实例对象查找属性时, 会先查找实例属性, 不存在则查找类属性
print(Car.wheel)

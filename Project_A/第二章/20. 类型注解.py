# 指定类型注解 (未指定的话解释器会根据你赋的值进行类型推断)
a: int = 2
list1: list[str | int] = ["a", 2, 3]
dict1: dict[str, int] = {"a": 1, "b": 2}
tuple1: tuple[str, int] = ("a", 1)

def shopping(*args: tuple[str, float, int], coupon = 0, points = 0, express = 0.0) -> float:      # 函数返回值类型: (参数) -> 类型
    price = sum([item[1] * item[2] for item in args])
    if coupon <= price and price > 5000:
        price -= coupon
    if points // 100 < price and price > 5000:
        price -= points // 100
    return price + express

print(shopping(("笔", 2, 200), ("运动饮料", 4, 200), ("打印机", 5000, 1), coupon = 1500, points = 6000, express = 50))
print(shopping(("笔", 2, 400), ("运动饮料", 4, 100), ("打印机", 5000, 1), express = 10))
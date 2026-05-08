# 案例: 基于match...case实现一个游戏角色控制系统
move = input("请输入移动指令: ")
match move:
    case "w" | "W":
        print("角色向前移动")
    case "s" | "S":
        print("角色向后移动")
    case "a" | "A":
        print("角色向左移动")
    case "d" | "D":
        print("角色向右移动")
    case " ":
        print("角色跳跃")
    case _:
        print("不进行移动")

# 案例: 基于match...case实现一个简易乘除法计算器
num1 = int(input("请输入被除数: "))
num2 = int(input("请输入除数: "))
sign = input("请输入符号: ")
match sign:
    case "*":
        print(f"结果为{num1 * num2}")
    case"/" if num2 != 0:       # if条件成立才匹配该case
        print(f"结果为{num1 / num2}")
    case _:
        print("结果无效")
# 函数内为局部变量, 需要操作全局变量用global, 先声明后使用
global_x = "全局变量"
print(global_x)

def global_test():
    global global_x
    global_x = "全局变量已改变"
    return global_x

global_test()
print(global_x)

# 传参方式一: 位置参数 (根据函数定义时的位置来传递参数)
def function(name, age, location = "中国"):                   # 默认参数: 未传递该参数时, 调用默认值
    print(f"{name}, {age}岁, 家住{location}")                      # 默认参数必须放在没有默认值的参数后

function("张三", 20, "北京")

# 传参方式二: 关键字参数 (以"键 = 值"的形式传递参数)
function(age = 28, name = "李四", location = "上海")

# 传参方式三: 位置参数 + 关键字参数 (关键字参数在位置参数之后)
function("王五", location = "香港", age = 35)

# 参数不超过3个, 使用位置参数, 否则使用关键字参数
# 如果不能一眼看出参数含义, 就应使用关键字参数

# 不定长参数
# 位置参数 *args (元组类型)
def calcu_data(*args):
    return min(args), max(args)

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(calcu_data(*data_list))                                       # 函数接收多个独立位置参数时，列表要解包
print(calcu_data(1, 2, 3, 4, 5))

# 关键字参数 **kwargs (字典类型)
def calcu_data(*args, **kwargs):                                    # 两不定长参数同时存在, 先定义位置参数
    min_data = min(args)
    max_data = max(args)
    ave = sum(args) / len(args)
    if kwargs.get("round") is not None:
        ave = round(ave, kwargs.get("round"))
    if kwargs.get("print"):
        print(f"最小值为{min_data}, 最大值为{max_data}, 平均值为{ave}")
    return min_data, max_data, ave

print(calcu_data(1, 2, 3, 4, 5, 6, 7, 8, 15))
print(calcu_data(1, 2, 3, 4, 5, 6, 7, 8, 15, round = 3, print = True))



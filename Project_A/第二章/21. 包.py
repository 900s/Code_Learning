# 导入模块
# import utils.my_fun
# print(utils.my_fun.multiply(2,3))
# from utils import my_fun
# print(my_fun.multiply(2,3))

# 注意: 在通过 from 包名 import * 导入全部模块时, 需要在__init__.py 文件中添加 __all__ = [] 控制允许导入的模块列表
from utils import *
print(my_fun.divide(4, 2))
print(my_var.speed_of_light)

# 导入模块中的功能
# 相对路径写法 (从当前文件所在目录查找)
# from utils.my_fun import divide, multiply

# 绝对路径写法 (从项目的根目录下开始查找)
# from 第二章.utils.my_fun import divide, multiply
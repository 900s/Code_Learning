__all__ = ["count_num", "earth_radius"]     # __all__: 指定 from 模块 import * 时导入哪些功能

PI = 3.1415926
earth_radius = 6371.0

def count_num(s):
    num = len(s)
    return num

# 函数调试 (被当做模块导入时, 以下代码不执行)
print(__name__)                             # 当该模块被导入时, __name__的值为模块的文件名
if __name__ == '__main__':                  # __name__: Python内置变量, 运行当前模块__name__的值为"__main__"
    print(count_num('hello'))

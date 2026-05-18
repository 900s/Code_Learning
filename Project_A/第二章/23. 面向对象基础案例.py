# 采用面向对象编程思想, 完成教务管理系统开发
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"姓名: {self.name} | 语文: {self.chinese} | 数学: {self.math} | 英语: {self.english} | 总分: {self.english + self.math + self.chinese}"

class TeachingSystem:
    version = "1.0.0"
    def __init__(self):
        self.student_list = []

    def run(self):
        """
        教务系统交互界面实现
        """
        while True:
            print("""
                                               欢迎使用教务管理系统!
            #########################################################################################################
            1. 添加学生成绩   2. 修改学生成绩   3. 删除学生成绩   4. 查询学生成绩   5. 展示全部学生成绩   6. 退出系统
            #########################################################################################################
            """)
            num = input("\n请输入1-6选择想使用的功能: ")
            # 异常传递: 异常在函数调用中层层上报的过程
            try:                # 哪里会出现异常, try就放在哪 (放在最上层, 代码更少更集中)
                match num:
                    case "1":
                        self.add()
                    case "2":
                        self.modify()
                    case "3":
                        self.delete()
                    case "4":
                        self.search()
                    case "5":
                        self.show()
                    case "6":
                        print("感谢使用教务管理系统, 祝您生活愉快!")
                        break
                    case _:
                        print("非法操作, 请重新输入!")
            except ValueError:
                print("只能输入整数, 请重新输入!")
            except Exception:
                print("出现错误, 请联系管理员!")

    def add(self):
        """
        添加学生成绩: 根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中,
        检查学生姓名是否存在, 不存在则添加, 并验证成绩范围
        """
        name = input("请输入学生姓名: ")
        for s in self.student_list:
            if name == s.name:
                print("该学生已存在, 添加失败!")
                return
        while True:
            chinese = int(input("请输入学生语文成绩: "))
            math = int(input("请输入学生数学成绩: "))
            english = int(input("请输入学生英语成绩: "))
            if chinese in range(0, 101) and math in range(0, 101) and english in range(0, 101):
                student = Student(name, chinese, math, english)
                self.student_list.append(student)
                print("学生信息添加成功!")
                return
            else:
                print("各科成绩必须在0-100之间! 添加失败")

    def modify(self):
        """
        修改学生成绩：根据输入的学生姓名，修改对应的学生成绩,
        显示该生当前信息, 输入新的成绩后更新学生成绩
        """
        name = input("请输入要修改的学生姓名: ")
        for s in self.student_list:
            if name == s.name:
                print(f"该学生信息: {s}")
                while True:
                    chinese = int(input("请输入修改后的学生语文成绩: "))
                    math = int(input("请输入修改后的学生数学成绩: "))
                    english = int(input("请输入修改后的学生英语成绩: "))
                    if chinese in range(0, 101) and math in range(0, 101) and english in range(0, 101):
                        s.chinese = chinese
                        s.math = math
                        s.english = english
                        print("信息修改成功!")
                        print(f"该学生现在的信息:{s}")
                        return
                    else:
                        print("各科成绩必须在0-100之间! 添加失败")
        print("未找到该学生, 修改失败!")

    def delete(self):
        """
        删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
        """
        name = input("请输入要删除的学生姓名: ")
        for s in self.student_list:
            if name == s.name:
                self.student_list.remove(s)
                print("删除成功!")
                return
        print("未找到该学生, 删除失败!")

    def search(self):
        """
        查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
        """
        name = input("请输入想查询的学生姓名: ")
        for s in self.student_list:
            if name == s.name:
                print(f"查询结果: {s}")
                return
        print("未找到该学生, 查询失败!")

    def show(self):
        """
        展示全部学生成绩：展示出系统中所有学生的成绩
        """
        for s in self.student_list:
            print(s)

# 调试案例
if __name__ == "__main__":
    teaching_system = TeachingSystem()
    teaching_system.run()





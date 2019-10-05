# Author：George Ling

# def stu_register(name, age, country, course):
def stu_register(name, age, course, country="CN"):
    print("----注册学生信息------")
    print("姓名:", name)
    print("age:", age)
    print("国籍:", country)
    print("课程:", course)


stu_register("王山炮", 22, "python_devops")
stu_register("张叫春", 21, "linux")
stu_register("刘老根", 25, "linux")

# 默认参数特点：调用函数时，默认参数非必须传递
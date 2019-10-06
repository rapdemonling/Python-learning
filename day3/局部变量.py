# Author：George Ling

hobby = 'basketball' #全局变量

def change_name(name):
    global hobby #改全局变量(尽量不用)
    hobby = "python" #局部变量
    print("before_change",name,hobby)
    name = "George Ling" #局部变量作用域
    print("after_change",name)

name = 'ling'
change_name(name)
print(name)
print(hobby) #全局变量

# 全局与局部变量
#
# 在子程序中定义的变量称为局部变量，在程序的一开始定义的变量称为全局变量。
# 全局变量作用域是整个程序，局部变量作用域是定义该变量的子程序。
# 当全局变量与局部变量同名时：
# 在定义局部变量的子程序内，局部变量起作用；在其它地方全局变量起作用。
# Author：George Ling

a, b = 5, 8
c = a ** b
print(c)

# 改成用函数写
def calc(x, y):
    res = x ** y
    return res  # 返回函数执行结果

c = calc(a,b)
print(c)
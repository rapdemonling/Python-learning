# Author：George Ling

def test(x,y,z=2):
    print(x)
    print(y)
    print(z)

test(1,2,3)

# *args接收N个位置参数，转化成元组的方式
def test2(*args):
    print(args)

test2(1,2,3,4,5)
test2(*[1,2,3,4,5])

# **kwargs接收N个关键参数，转化成字典的方式
def test3(name,**kwargs):
    print(name)
    print(kwargs)

test3('ling',age=20,sex='M')
test3('yao',age=30,sex='M')
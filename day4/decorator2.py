# Author：George Ling

# 高阶函数
# a:把一个函数名当作实参传给另外一个函数
# b:返回值中包含函数名（不修改函数的调用方式）
'''
import time

def bar():
    time.sleep(3)
    print('in the bar')

def test1(func):
    start_time = time.time()
    func()  # run bar
    stop_time = time.time()
    print('the func run time is %s' % (stop_time - start_time))

test1(bar)
'''

import time
def bar():
    time.sleep(3)
    print('in the bar')

def test2(func):
    print(func)
    return func

# print(test2(bar))
bar = test2(bar)
bar() #run bar
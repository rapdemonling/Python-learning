# Author：George Ling

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n = n + 1
    return '---done---'

f = fib(10)
print(f.__next__())
print(f.__next__())
print("-----------") #跳出函数循环
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
# Author：George Ling

def add(x, y, f):
    return f(x) + f(y)


res = add(3, -6, abs)
print(res)
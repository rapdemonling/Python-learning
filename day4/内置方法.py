# Author：George Ling

# https://docs.python.org/3/library/functions.html?highlight=built

'''
print(all([1,-5,3]))
print(any([]))
print(ascii(["我没有","开挂"]))
print(bin(265))
print(chr(98))
print(ord('b'))

def sayhi(n):
    print(n)
    for i in range(n):
       print(i)
sayhi(3)

# lambda n:print(n))(5)
calc = lambda n:3 if n<4 else n
print(calc(5))
'''

'''
# res = filter(lambda n:n>5,range(10))
res = map(lambda n:n**n,range(10))
for i in res:
    print(i)
'''

# import functools
# res = functools.reduce( lambda x,y:x+y,range(1,10))
# print(res)


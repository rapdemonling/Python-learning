# Author：George Ling

# 可以直接作用于for循环的数据类型有以下几种：
# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

from collections import Iterator
a = isinstance((x for x in range(10)), Iterator)
print(a)
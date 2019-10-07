# Author：George Ling

# 生成器
# 通过列表生成式，我们可以直接创建一个列表。
# 但是，受到内存限制，列表容量肯定是有限的。
# 如果我们仅仅需要访问前面几个元素，那后面元素占用的空间都浪费了。
#
# 在Python中，一边循环一边计算的机制，称为生成器：generator。

a = [i*2 for i in range(10)]
print(a)

c = (i*2 for i in range(10)) #生成器生成地址，只有在调用时才生成数据
print(c)
for i in c:
    print(i)
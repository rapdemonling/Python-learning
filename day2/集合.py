# Author：George Ling

list_1 = [1,4,5,7,3,6,7,9]
list_1 = set(list_1)

print(list_1,type(list_1))

list_2 = set([2,6,0,66,22,8,4])
print(list_1,list_2)

# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
# 并集
print(list_1.union(list_2))
print(list_1 | list_2)

# 差集
print(list_1.difference(list_2))
print(list_1 - list_2)
# 子集
list_3 = set([1,3,7])
print(list_3.issubset(list_1))
# 对称差集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)

# 添加删除
list_1.add(999)
list_1.update([888,777,555])
list_1.remove(777)
print(list_1)


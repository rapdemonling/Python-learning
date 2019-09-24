# Author：George Ling

import copy

person = ['name',['saving',100]]
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)
'''
p1 = person[:]
p2 = person[:]

p1[0] = "GeorgeLing"
p2[0] = "MichealJordan"

p1[1][1] = 50 #联合账号

print(p1)
print(p2)
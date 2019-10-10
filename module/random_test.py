# Author：George Ling

import random

print (random.random())
print (random.randint(1,2))
print (random.randrange(1,10))

checkcode = ''
for i in range(4):
    current = random.randrange(0,4)
    if current != i:
        temp = chr(random.randint(65,90))
    else:
        temp = random.randint(0,9)
    checkcode += str(temp)
print (checkcode)
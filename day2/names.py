# Author：George Ling

# names = "GeorgeLing KobeBryant MichealJodan DerrickRose"
names = ["GeorgeLing", "KobeBryant", "MichealJodan", "DerrickRose"]
names.append("LebronJames")
names.insert(1,"StevenCurry")
names.insert(3,"ChrisPaul")
names[2] = "KlayTompson"

# print(names)
# print(names[0],names[2])
# print(names[1:3])
# print(names[-1]) #切片
# print(names[-2:]) #切片
# print(names[:3]) #切片

# delete
# names.remove("DerrickRose")
# del names[1] = names.pop(1)
# names.pop(1)
# print(names)
# print(names.index("MichealJodan"))
# print(   names[names.index("MichealJodan")]   )

# print(names.count("MichealJodan"))
# names.clear()
# names.reverse()
# print(names)
#
# names2 = [1,2,3,4]
# names.extend(names2)
# print(names,names2)

# name2 = names.copy()
# print(names)
# print(name2)

# import copy

# name2 = copy.deepcopy(names)
# print(names)
# print(name2)

print(names[0:-1:2])
print(names[::2])
print(names[:])
# for i in names:
#     print(i)
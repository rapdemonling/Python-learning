# Author：George Ling

info = {
    'stu1101': "George Ling",
    'stu1102': "Micheal Jordan",
    'stu1103': "Chris Paul",
}

#通过一个列表生成默认dict
dict.fromkeys([1,2,3],'testd')
{1: 'testd', 2: 'testd', 3: 'testd'}

info["stu1101"] = "凌"
info["stu1104"] = "布里克·格里芬"

print(info.get('stu1103'))
print('stu1103' in info)

# del info["stu1101"]
info.pop("stu1101")
info.popitem()
print(info)


# 字典循环：

#方法1
for key in info:
    print(key,info[key])

#方法2
for k,v in info.items(): #会先把dict转成list,数据里大时莫用
    print(k,v)
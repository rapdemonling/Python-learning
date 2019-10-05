# Author：George Ling

# data = open('yesterday',encoding="utf-8").read()  # 打开文件
f = open('yesterday','r',encoding="utf-8")  #文件句柄

# f.write("我爱学习,\n")
# f.write("学习使我快乐")
# f.write("我爱学习!!!\n")
# f.write("学习使我快乐!!!")

# data = f.read()
# print(data)  # 打印文件
#
# f.close()  # 关闭文件

'''
for index,line in enumerate(f.readlines()):
    if count == 9:
        print('-----我是分割线-----')
        continue
    print(line.strip())
'''

count = 0
for line in f:
    if count == 9:
        print('-----我是分割线-----')
        count+=1
        continue
    print(line)
    count +=1
# Author：George Ling
'''
import sys

# print(sys.path)

print(sys.argv)

print(sys.argv[2])
'''
'''
import os

# cmd_res = os.system("dir") #执行命令，不保存结果
cmd_res = os.popen("dir").read()#执行命令，保存结果

print("-->",cmd_res)
os.mkdir("new_dir")
'''
# import login

msg = "我爱学习！"

print(msg)

print(msg.encode(encoding="utf-8"))
print(msg.encode(encoding="utf-8").decode(encoding="utf-8"))

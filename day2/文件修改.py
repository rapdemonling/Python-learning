# Author：George Ling

f = open("yesterday2","r",encoding="utf-8")
f_new = open("yesterday2.bak","w",encoding="utf-8")

for line in f:
    if "肆意的快乐等我享受" in line:
        line = line.replace("肆意的快乐等我享受","肆意的快乐等ling享受")
    f_new.write(line)
f.close()
f_new.close()
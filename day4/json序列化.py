# Author：George Ling
# import json
import pickle

def sayhi(name):
    print("hello,",name)

info = {
    'name':'ling',
    'age':22,
    'func':sayhi
}

f= open("test.test","wb")
# print(json.dumps((info)))
# f.write(json.dumps(info))
print(pickle.dumps((info)))
# f.write(pickle.dumps(info))
pickle.dump(info,f)
f.close()

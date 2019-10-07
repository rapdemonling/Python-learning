# Author：George Ling
import json
# import pickle

def sayhi(name):
    print("hello2,",name)

f= open("test.test","r")

data = json.loads(f.read())
# data = pickle.loads(f.read())
# data = pickle.load(f)
print(data['age'])

print(data["func"]("ling"))

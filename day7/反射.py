__author__ = "George Ling"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)

d = Dog("旺财")
choice = input(">>:").strip()

if hasattr(d,choice):
    getattr(d,choice)
else:
    setattr(d,choice,bulk) #d.talk = bulk
    func = getattr(d, choice)
    func(d)


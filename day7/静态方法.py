__author__ = "George Ling"

import os
# os.system()
# os.mkdir()

class Dog(object):
    def __init__(self,name):
        self.name = name

    @staticmethod #跟类没什么关系
    def eat(self):
        print("%s is eating %s" %(self.name,'bone'))

    def talk(self):
        print("%s is barking"% self.name)
d = Dog("旺财")
d.eat(d)
d.talk()
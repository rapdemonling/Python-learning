__author__ = "George Ling"


class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        pass #raise NotImplementedError("Subclass must implement abstract method")

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Cat(Animal):
    def talk(self):
        print('Meow!')


class Dog(Animal):
    def talk(self):
        print('Woof! Woof!')


d = Dog("旺财")
#d.talk()

c = Cat("咪咪")
#c.talk()
#
# def animal_talk(obj):
#     obj.talk()

Animal.animal_talk(c)
Animal.animal_talk(d)


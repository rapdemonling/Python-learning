# Author：George Ling

# 嵌套函数
# a:在一个函数内部申明另一个函数

'''
def foo():
    print('in the foo')
    def bar():
        print('in the bar')

    bar()
foo()
'''

x = 0
def grandpa():
    x=1
    def dad():
        # x=2
        def son():
            # x=3
            print(x)
        son()
    dad()
grandpa()


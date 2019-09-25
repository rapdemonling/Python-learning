# Author：George Ling

name = "my name is {name} and i'm {year} old."

print(name.capitalize())
print(name.count("a"))
print(name.center(50,"-"))
print(name.endswith("ge"))
print(name.expandtabs())

print(name.format(name='George',year=18))
print(name.format_map( {'name':'George','year':18}  ))

print('1A'.isidentifier()) #判断是不是一个合法的标识符
print('A1'.isidentifier()) #判断是不是一个合法的标识符
print('My Name Is '.isupper()) #判断是不是大写

print('+'.join(['1','2','3','4'])  )
print('George'.upper())

print('George Ling'.replace('i','I',1))
print('George Ling'.split('i'))
print('1+2+3+4'.split('+'))
print('George Ling'.zfill(16))

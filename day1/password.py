# Author：George Ling
import getpass

_username = 'ling'
_password = 'abc123'

username = input("username:")
# password = getpass.getpass("password:")
password = input("password:")

if _username == username and _password == password:
    print("欢迎 {name} 登录...".format(name=username))
else:
    print("密码错误!")


# print(username,password)




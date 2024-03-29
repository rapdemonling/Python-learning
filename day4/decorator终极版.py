# Author：George Ling

# 语法糖
import time
user,passwd = 'ling','abc123'
def auth(auth_type):
    print("auth func:",auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()
                if user == username and passwd ==password:
                    print("\033[32;1mUser has passed authentication\033[0m")
                    res = func(*args,**kwargs)
                    print("---after authentication")
                    return res
                else:
                    exit("\033[32;1mInvalid username or password\033[0m")
            elif auth_type == "ldap":
                print("还不会")
        return wrapper
    return outer_wrapper

def index():
    print("welcome to index page")
@auth(auth_type="local")
def home():
    print("welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

index()
home()
bbs()

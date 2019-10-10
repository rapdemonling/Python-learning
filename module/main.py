# Author：George Ling

from module_ling import *

# import module_ling
# module_ling=all_code module_ling.name module_ling.logger()
import sys,os
print(sys.path)

x=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(x)
import module_ling

say_hello()

# Author：George Ling

'''
re.match
# 从头开始匹配
re.search
# 匹配包含
re.findall
# 把所有匹配到的字符放到以列表中的元素返回
re.splitall
# 以匹配到的字符当做列表分隔符
re.sub
# 匹配字符并替换
'''

import re
print(re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})","371481199306143242").groupdict("city"))

print(re.search("(?P<id>[0-9+])","abxhs12123412"))

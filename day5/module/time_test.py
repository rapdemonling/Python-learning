# Author：George Ling

import time

# print(time.process_time()) #返回处理器时间
# print(time.altzone)  #返回与utc时间的时间差,以秒计算\
# print(time.asctime()) #返回时间格式"Thu Oct 10 20:39:03 2019",
# print(time.localtime()) #返回本地时间 的struct time对象格式
# print(time.gmtime(time.time()-800000)) #返回utc时间的struc时间对象格式

# print(time.asctime(time.localtime())) #返回时间格式"Thu Oct 10 20:39:03 2019"
# print(time.ctime()) #返回Thu Oct 10 20:39:03 2019 格式, 同上



# 日期字符串 转成  时间戳
# string_2_struct = time.strptime("2019/10/10","%Y/%m/%d") #将 日期字符串 转成 struct时间对象格式
# print(string_2_struct)
#
# struct_2_stamp = time.mktime(string_2_struct) #将struct时间对象转成时间戳
# print(struct_2_stamp)



#将时间戳转为字符串格式
# print(time.gmtime(time.time()-86640)) #将utc时间戳转换成struct_time格式
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime()) ) #将utc struct_time格式转成指定的字符串格式


#时间加减
import datetime

# print(datetime.datetime.now()) #返回 2019-10-10 20:41:38.334257
# print(datetime.date.fromtimestamp(time.time()) )  # 时间戳直接转成日期格式 2019-10-10
# print(datetime.datetime.now() )
# print(datetime.datetime.now() + datetime.timedelta(3)) #当前时间+3天
# print(datetime.datetime.now() + datetime.timedelta(-3)) #当前时间-3天
# print(datetime.datetime.now() + datetime.timedelta(hours=3)) #当前时间+3小时
# print(datetime.datetime.now() + datetime.timedelta(minutes=30)) #当前时间+30分


c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2)) #时间替换
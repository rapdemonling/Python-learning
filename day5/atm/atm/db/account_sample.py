#!_*_coding:utf-8_*_
#__author__:"George Ling"


import json
acc_dic = {
    'id': ling,
    'password': 'abc123',
    'credit': 30000,
    'balance': 20000,
    'enroll_date': '2017-01-02',
    'expire_date': '2022-01-01',
    'pay_day': 22,
    'status': 0 # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(acc_dic))
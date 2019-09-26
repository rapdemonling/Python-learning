# Author：George Ling

data = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


exit_flag = False

while not exit_flag:
    for k in data:
        print(k)
    choice = input(">>1:")
    if choice in data:
        while not exit_flag:
            for i2 in data[choice]:
                print("\t",i2)
            choice2 = input(">>2:")
            if choice2 in data[choice]:
                while not exit_flag:
                    for i3 in data[choice][choice2]:
                        print("\t\t",i3)
                    choice3 = input(">>3:")
                    if choice3 in data[choice][choice2]:
                        for i4 in data[choice][choice2][choice3]:
                            print("\t\t",i4)
                        choice4 = input("最后一层，输入b返回>>：")
                        if choice4 == "b":
                            pass
                        elif choice4 == "q":
                            exit_flag = True
                    if choice3 == "b":
                        pass
                    elif choice3 == "q":
                        exit_flag = True
                if choice2 == "b":
                    pass
                if choice2 == "q":
                    exit_flag = True
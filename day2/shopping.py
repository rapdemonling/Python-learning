# Author：George Ling

product_list = [
    ('Iphone',6000),
    ('Macbook Pro',12000),
    ('HuaWei P30',4500),
    ('IWatch',4000),
    ('Coffee',32),
    ('Book',58),
]
shopping_list=[]
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            # print(product_list.index(item),item)
            print(index,item)
        user_choice = input("你要买啥？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Add %s into shopping cart, your current balance is \033[31;1m%s\033[0m" %(p_item,salary))
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，钱不够了。。。\033[0m" % salary)
            else:
                print("没有这种商品！")
        elif user_choice == 'quit':
            print("-----shopping list-----")
            for p in shopping_list:
                print(p)
            print("可用余额是：",salary)
            exit()
        else:
            print("无效命令")
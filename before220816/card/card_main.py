'''
Author: Xudi
Date: 2022-06-25 16:43
LastEditTime: 2022-07-01 16:12
FilePath: \pythonStudy\card\card_main.py
Description: 名片管理系统的主要使用框架
'''
import card_tools
while True:
    print("-" * 50)
    print("欢迎使用名片管理系统 v 1.0")
    print("1. 新建名片")
    print("2. 显示全部名片")
    print("3. 查询名片")
    print("0. 退出系统")
    order_input = input("请输入想要执行的功能：")
    if order_input in ["1","2","3","0"]:
        # 1.新建名片
        if order_input == "1":
            card_tools.list_table(card_tools.create_new())
            print("添加成功！")
        # 2.显示全部名片
        elif order_input == "2":
            card_tools.list_table(card_tools.show_card())
        # 3. 查询名片并对名片进行操作
        elif order_input == "3":
            name_search = input("请输入想要查询名片的姓名：")
            name_find = card_tools.search_card(name_search)
            if len(name_find) == 0:
                print("不好意思没有该名片！")
            else:
                card_tools.list_table(name_find)
                print("查询成功！")
                print("1. 修改名片 2.删除名片 0.退出")
                card_deal = input("请选择您要继续的操作！:")
                #  1. 修改名片
                if card_deal == "1":
                    card_tools.del_list(name_search)
                    card_tools.list_table(card_tools.deal_list(name_find))
                    print("修改成功！")
                # 2. 删除名片
                elif card_deal == "2":
                    print("删除之后的列表为：")
                    card_tools.list_table(card_tools.del_list(name_search))
                    print("删除成功！")
                # 0. 退出
                else:
                    pass
        # 0. 退出系统
        else:
            print("退出系统！")
            print("-" * 50)
            break
    else:
        print("请输入正确的数字。")
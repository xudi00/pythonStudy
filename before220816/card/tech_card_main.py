'''
Author: Xudi
Date: 2022-06-25 16:43
LastEditTime: 2022-07-01 17:08
FilePath: \pythonStudy\card\tech_card_main.py
Description: 名片管理系统的主要使用框架
'''
import tech_card_tools
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
            tech_card_tools.list_table(tech_card_tools.create_new())
            print("添加成功！")
        # 2.显示全部名片
        elif order_input == "2":
            tech_card_tools.list_table(tech_card_tools.show_card())
        # 3. 查询名片并对名片进行操作
        elif order_input == "3":
            tech_card_tools.search_card()
        # 0. 退出系统
        else:
            print("退出系统！")
            print("-" * 50)
            break
    else:
        print("请输入正确的数字。")
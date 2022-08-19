'''
Author: Xudi
Date: 2022-06-25 16:43
LastEditTime: 2022-07-01 16:15
FilePath: \pythonStudy\card\card_tools.py
Description: 名片管理系统的辅助功能
'''
from hashlib import new
from unittest import result


card_list= [{"name":"name", "age":"age", "phone":"phone", "email":"email"},\
    {"name":"123", "age":"12", "phone":"1234356", "email":"asdhihaui@maol.edu"}]

def list_table(change_list): 

    print('=' * 80)
    for i in ["姓名", "年龄", "电话", "邮箱"]:
        print(i,end='\t\t')
    print()
    print("-" * 80)
    for elem in change_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (elem["name"],elem["age"],elem["phone"],elem["email"]))
    print('=' * 80)
    return

def create_new():

    new_list = []
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    phone = input('请输入电话：')
    email = input('请输入邮箱：')
    new_list = [{"name":name, "age":age, "phone":phone, "email":email}]
    card_list.extend(new_list)
    return new_list

def show_card():

    return card_list


def search_card():
    '''
    description: 查找列表
    param {*} 
    return {*} 返回找到的列表
    '''
    name_search = input("请输入想要查询名片的姓名：")
    search_list = []
    for elem in card_list:
        if elem["name"] == name_search:
            search_list.append(elem)
            search_dict = elem
    if len(search_list) == 0:
        print("不好意思没有该%s名片！" % name_search)
    else:
        list_table(search_list)
        print("查询成功！【1】. 修改名片 【2】.删除名片 【0】.退出系统")
        card_deal = input("请选择您要继续的操作！:")
        # 1. 修改名片
        if card_deal == "1":
            search_dict["name"] = input_card_info(search_dict["name"],"请输入姓名")
            search_dict["age"] = input_card_info(search_dict["age"],"请输入年龄")
            search_dict["phone"] = input_card_info(search_dict["phone"],"请输入电话")
            search_dict["email"] = input_card_info(search_dict["email"],"请输入邮箱")
            list_table(card_list)
            print("修改成功！")
        # 2. 删除名片
        elif card_deal == "2":
            card_list.remove(search_dict)
            print("删除成功！")
        # 0. 退出
        else:
            pass
    

def del_list(name_input):
    for i,elem in enumerate(card_list):
        if elem["name"] == name_input:
            card_list.pop(i)
    return card_list

def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)

    if len(result_str) > 0:
        return result_str
    else:
        return dict_value

'''
def deal_list(old_list:list):
    name = input('请输入修改的姓名，不修改请按回车：')
    age = input('请输入修改的年龄，不修改请按回车：')
    phone = input('请输入修改的电话，不修改请按回车：')
    email = input('请输入修改的邮箱，不修改请按回车：')
    new_dict = {"name":name, "age":age, "phone":phone, "email":email}
    if len(new_dict["name"])== 0:
        new_dict["name"]=old_list[0]["name"]
    if len(new_dict["age"])== 0:
        new_dict["age"]=old_list[0]["age"]
    if len(new_dict["phone"])== 0:
        new_dict["phone"]=old_list[0]["phone"]
    if len(new_dict["email"])== 0:
        new_dict["email"]=old_list[0]["email"]
    new_list = []
    new_list.append(new_dict)
    card_list.extend(new_list)
    return new_list
'''
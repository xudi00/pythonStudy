'''
Author: Xudi
Date: 2022-06-25 16:43
LastEditTime: 2022-06-28 20:59
FilePath: \pythonStudy\card\card_tools.py
Description: 名片管理系统的辅助功能
'''
card_list= [{"name":"name", "age":"age", "phone":"phone", "email":"email"},\
    {"name":"123", "age":"12", "phone":"1234356", "email":"asdhihaui@maol.edu"}]

def list_table(change_list): 
    '''
    description: 修改列表成打印格式
    param {*} change_list 要修改的列表
    return {*} 打印列表
    '''
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
    '''
    description: 创建新的名片
    return {*} 返回含新名片的列表
    '''    
    new_list = []
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    phone = input('请输入电话：')
    email = input('请输入邮箱：')
    new_list = [{"name":name, "age":age, "phone":phone, "email":email}]
    card_list.extend(new_list)
    return new_list

def show_card():
    '''
    description: 
    return {*} 返回名片列表
    '''    
    return card_list


def search_card(name_input):
    '''
    description: 查找列表
    param {*} name_input 输入要查找的名字
    return {*} 返回找到的列表
    '''
    search_list = []
    for elem in card_list:
        if elem["name"] == name_input:
            search_list.append(elem)
    return search_list

def del_list(name_input):
    '''
    description: 删除有该名字的名片，并输出打印删除之后的列表
    param {*} name_input 要删除的名片的名字
    return {*}
    '''
    for i,elem in enumerate(card_list):
        if elem["name"] == name_input:
            card_list.pop(i)
    return card_list
# -*- coding: UTF8 -*-
"""
@Project        ：pythonStudy 
@File           ：duplicate.py
@Author         ：Di Xu
@Date           ：2022/8/9 15:29
@Description    : python对于文件操作的测试，利用ReadLine将文件全部打印出来
"""
# 1. 打开文件
file = open("data.txt")
file2 = open("data2.txt","w")
# 2. 读取并写入文件
while True:
    # 读取一行值
    value = file.readline()
    print(not value)
    # 判断是否读取到内容是否为空
    if not value:
        break
    # 写入一行值
    file2.write(value)
# 3.关闭文件
file.close()
file2.close()
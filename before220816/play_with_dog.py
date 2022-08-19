# -*- coding: UTF8 -*-
"""
@Project        ：pythonStudy 
@File           ：play_with_dog.py
@Author         ：X.D.
@Date           ：2022/8/8 17:34
@Description    : 练习继承的py代码
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 汪汪叫的玩耍..." % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s 在天上玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        print("%s 和 %s 一起玩耍..." % (self.name, dog.name))
        dog.game()


# 1. dog
wangcai = XiaoTianQuan("旺财")

# 2. person
xiaoming = Person("小明")

# 3.play
xiaoming.play_with_dog(wangcai)

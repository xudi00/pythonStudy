# -*- coding: UTF8 -*-
"""
@Project        ：pythonStudy 
@File           ：once_init_model.py
@Author         ：X.D.
@Date           ：2022/8/8 19:51
@Description    : 单例设计模式练习，只有一个实例的类。
"""


class Player(object):
    # if created
    instance = None

    # count
    def __new__(cls, *args, **kwargs):
        # 1.判断地址是否为空值
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


# 创造两个实例，判断其地址是否相同
print(Player.instance)
music1 = Player()
print(Player.instance)
music2 = Player()
print(Player.instance)
print(id(music1))
print(id(music2))

# 摇骰子,使用可变参数
# random是模块
# randint是函数
import random as m1

def main():
    def roll():
        return m1.randint(1,6)
    def add(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    print(add(1,2,3,4,5,6))

if __name__ =='__main__':
    main()
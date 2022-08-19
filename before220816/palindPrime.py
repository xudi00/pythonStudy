'''
判断一个数是不是回文数\罗素数
'''

from math import sqrt


def main():
    def is_palind(number):
        before = number
        after = 0
        while number > 0:
            after = after*10 + number % 10
            number = number // 10
        return True if before == after else False
    
    def is_prime(number):

# int(sqrt(number))的写法不对，会报错，可以直接用阶乘

        is_prime = True
        for i in range(2,int(number ** 0.5 )+1):
            if number % i == 0:
                is_prime = False
        return is_prime if number != 1 else False

# 可以直接return打断for循环

    x = int(input('x='))
    print(is_palind(x) and is_prime(x))

if __name__ == '__main__':
    main()
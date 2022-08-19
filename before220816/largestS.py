# 求最大公约数和最小公倍数

def main():
    def largest(m,n):
        (m,n) = (n,m) if m > n else (m,n)
        for i in range(m,0,-1):
            if m % i == 0 and n % i == 0:
                return i

# 运算符中//表示整除 除以一个数等于0不存在

    def smallest(m,n):
        return m*n//largest(m,n)

    x = int(input('x='))
    y = int(input('y='))

    print(largest(x,y),smallest(x,y))
if __name__ == "__main__":
    main()
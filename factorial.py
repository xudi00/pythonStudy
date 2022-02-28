# 输入M和N计算C(M,N)

def main():
    def multi(x):
        sum = 1
        for i in range(1,x+1):
            sum *= i
        return sum
    m = int(input('m='))
    n = int(input('n='))
    print(multi(m)//multi(n)//multi(m-n))

if __name__ == '__main__':
    main()
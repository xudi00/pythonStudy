# 全局作用域 局部作用域 内置作用域 嵌套作用域
def foo():
    a = 200
    b = "hello"

    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    
    bar()
    print(a) # a No problem
    # print(c)  not defined

if __name__ == "__main__":
    a = 100
    print(a)
    # print(b) not defined
    foo()

# 全局作用域 局部作用域内同名变量不是一个变量
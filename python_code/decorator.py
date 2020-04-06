# -*- coding: utf-8 -*-
import time

# 装饰器
# 装饰器是在函数定义时前面加@，然后跟装饰器的实现函数。可以看出，现在只要直接调用do_something就可以了。调用的地方不要作任何修改


# 统计函数的执行时间
# 每次调用的是decorator，还要把函数作为一个参数传入，使用起来就不方便了。
def decorator(fun):
    def wrapper():
        start = time.time()
        fun()
        runTime = time.time() - start
        print(runTime)
    return wrapper

@decorator
def do_something():
    for i in range(10000000):
        pass
    print("plag game")

# 带参数的装饰器,就是给wrapper函数参加相同的参数
def decorator02(fun):
    def wrapper02(name):
        start = time.time()
        fun(name)
        runTime = time.time() - start
        print(runTime)
    return wrapper02

@decorator02
def do_something02(name):
    for i in range(10000000):
        pass
    print("plag game" + name)

# 目标函数带不固定参数的装饰器
def decorator03(fun):
    def wrapper03(*args,**kwargs):
        start = time.time()
        fun(*args,**kwargs)
        runTime = time.time() - start
        print(runTime)
    return wrapper03

@decorator03
def do_something03(name):
    for i in range(10000000):
        pass
    print("plag game" + name)

@decorator03
def do_something04(user,name):
    for i in range(1000000):
        pass
    print(user + "play game" + name)

# 目标函数每次调用重复执行指定的次数
def decorator05(max):
    def _decorator(fun):
        def wrapper(*args,**kwargs):
            start = time.time()
            for i in range(max):
                fun(*args,**kwargs)
            runTime = time.time() - start
            print(runTime)
        return wrapper
    return _decorator

@decorator05(2)
def do_something05(name):
    for i in range(10000000):
        pass
    print("plag game" + name)


if __name__ == '__main__':
    #do_something()
    #do_something02("san guo sha")
    #do_something03(" hao ")
    #do_something04(" wo "," xiao ")
    do_something05(" ha ")

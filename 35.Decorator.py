# Functions are first class citizens in python
# That means they can be passed around like variables
def hello():
    print('Hello world')


greet = hello
greet()


def a(func):
    func()


def b():
    print('I am a Big B')


print(a(b))

# Higer order function: a function that takes another function as a parameter
# that's why fitler, map and reduce all are Higher order function as they accept another function
# or  A FUNCION that return another function


def greet(func):
    func()


def hof():
    def func():
        return 4
    return func

# a decorator supercharges another function
# it wraps another functins and proivides additional functionality to it


def myDecorator(func):
    def wrapper_func():
        print('*****')
        func()
        print('&&&&&')
    return wrapper_func


@myDecorator
def hello():
    print('hello')


hello()
# Why does it work???
# it becomes equivalent to
tempFunc = myDecorator(hello)
tempFunc()
# here the myDecorator actually wraps the hello function and the after
# wrapper it returns the new wrapped function which will be called through hello()

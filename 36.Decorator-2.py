# Decorator Patterm
from time import time


def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('------------')
        func(*args, **kwargs)
        print('------------')
    return wrap_func


@my_decorator
def hello(greeting, emoji=':)'):
    print(greeting, emoji)


hello('hi')

# A practical Example


def performance(func):
    def wrap_func():
        t1 = time()
        func()
        t2 = time()
        return t2-t1
    return wrap_func


@performance
def long_running_func():
    for i in range(99909999):
        i*5


x = long_running_func()
print('%f' % x)

# practical applications of decorator:
# for example
# @login decorator to check that login is required before executing the function
# @logging to log database operations etc

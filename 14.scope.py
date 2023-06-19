# Scope tells which variables I have access to
# GLobal scope vs the function scope
# Order of scope
# 1. local
# 2. Parent Local
# 3. Global
# 4. Built in Python function
# Scope helps the python garbage collector to free up the space once the function has completed running
# global keyword

total = 0


def add():
    global total  # tells to use the global variable
    total += 1
    return total


print(add())

# nonlocal


def add1():
    x = 'test'

    def minus():
        x = 'testmodified'
        print(x)
    return minus()


print(add1())

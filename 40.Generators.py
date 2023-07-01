# Generators allows us to generate a seqeunce of values over time
# 1. Difference between list and range (range does not create the items in the memory but the list does): range generates an item one at a time without taking up much memory (ch 163)
# Difference between iterable and generator,, iterable eg list, generator eg range (iterable is not a generator but a generator is a iterable)

range(100)
print(list(range(100)))


def genList(length):
    mylist = []
    for x in range(length):
        mylist.append(x**2)
    return mylist


print(genList(5))

# GENERATORS
# generators typeically loops over an range and yield the result which can be printer through next(gen func)


def generator_function(len):
    for i in range(len):
        yield i*2


g = generator_function(10)
next(g)
print(next(g))
print(next(g))
# for x in generator_function(10):
#     print(x)

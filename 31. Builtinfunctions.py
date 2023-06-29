# map, filter, zip and reduce
# my list is not modified but a new list is created by the map function
from functools import reduce
mylist = [1, 2, 3]


def multiplyby2(item):
    return item**2


print(list(map(multiplyby2, mylist)))
print(mylist)
# So as it create a new output without modifying the inputs and everytime we run for every inputs we get the same outpput
# TU UPPER
testList = ['mango', 'apple', 'banana']


def toUpper(item: str):
    return item.upper()


print(list(map(toUpper, testList)))

# FILTER will add only those items that pass the test otherwise it will be dropped and not added to the new list


def only_odds(item):
    return item % 2 != 0  # 3/2 1


print(list(filter(only_odds, [1, 2, 3, 4, 5, 6, 7])))

# ZIP:: zip iterates over each iterables and zips themup together into tuples one each from each list
my_list = [10, 20, 30, 40, 50]
your_list = [100, 200, 300, 400, 800]

print(list(zip(my_list, your_list)))

# REDUCE: reduce accumulates and reduces the entire iterable to a single value


def accumulator(acc, item):  # acc is the accumulator value that updates for each item but its start from 0 as set furing call
    return acc + item


print(reduce(accumulator, my_list, 0))

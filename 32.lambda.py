# lamda param: action(param)
# lambda function the interpreter doesn't need to remember the function
# it just execute, does its job and done and goes to the next line
# we just use them once and we dont have a name

from functools import reduce
my_list = [1, 2, 3, 3, 5]
print(list(map(lambda item: item*2, my_list)))

print(list(filter(lambda item: item % 2 == 0, [2, 5, 7, 9, 8])))
# with reduce
print(reduce(lambda acc, item: acc + item, my_list, 0))

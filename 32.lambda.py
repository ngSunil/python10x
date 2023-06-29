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

print(list(map(lambda item: item**2, my_list)))

a = [(0, 2), (15, 1), (9, 6), (10, -1)]
a.sort(key=lambda item: item[1])
print(a)

my_dict = [{
    'name': 'sunil',
    'address': 'ghy'
},
    {
    'name': 'anil',
    'address': 'titaber'
},
    {
    'name': 'rita',
    'address': 'numaligarh'
}]
my_dict.sort(key=lambda item: item['name'])
print(my_dict)

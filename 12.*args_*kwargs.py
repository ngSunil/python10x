# *args can take any number of arguments through a single parameter
# **kwargs will combine all the keyword arguments in to a dictionary
# parameter rule::: normalparameter, *args, keyword parameters, **kwargs
def func(*args, **kwargs):
    print(kwargs)
    total = 0
    for item in kwargs.values():
        total += item
    return sum(args, total)


print(func(1, 2.316, 9, num1=4, num2=10))

# HIGHEST EVEN PROBLEM:::


def highest_even(li):
    even_list = []
    for item in li:
        if item % 2 == 0:
            even_list.append(item)
    return max(even_list)


print(highest_even([10, 3, 5, 16, 4]))

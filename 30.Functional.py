# What is functional programming advantages:
# Clear and understandanle
# easy to extend
# easy to maintain
# memmory efficient
# DRY
# PURE FUNCTIONS: There is separation between the data of a program and behaviour of a program
# A function should always return the same output
# There should not be any sideeffects ie it should not interact with the outside world so printing functions should always return
# which will be printed later by calling in
# EG It is very useful to understand as the function will be separated from the outside world and wont be touched by the outside world
# whcih will be ease to debug and will be less error prone

def multiply2(li):
    result = []
    for i in li:
        result.append(i*2)
    return result  # This doesnt interact with the outside world, but if we had given print here than it would interact with the outside world and defy the pure functions


print(multiply2([1, 10, 100]))

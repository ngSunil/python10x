def check_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 != 0:
        return False


print(check_even(10))

#  butt  you can remove above code to make it more cleaner


def check_even1(num):
    if num % 2 == 0:
        return True
    return False


print(check_even1(11))
# and even more cleaner


def check_even2(num):
    return num % 2 == 0

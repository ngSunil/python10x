# positional arguments
def say_hello(name='Mighty Sunil', age=800):  # default parameters value
    print(f'Hello {name}, your age is {age}')


# say_hello()
# positional arguments
say_hello('Sunil 🥲', 34)

# keyword arguments
say_hello(name='ANil🤣', age=25)

# return statement


def sum(n1, n2):
    return n1+n2


print(sum(3, 5))

# a catch


def add(a, b):
    '''
    Info: The add function takes two argumnets and adds and returns them
    '''
    # return 100

    def sum1(a, b):
        return a+b
    return sum1(a, b)


# also tell that multiple return statement will cause below lines to not get executed (unreachable code)
print(add(10, 8))
sum
# METHODS VS FUNCTIONS
# if we give a . after the string or a list we can get the list of all the methods
# but unlike the functions like sum()
# both methods and functions allow us to take some actions
help(add)  # will print the document of the function
print(add.__doc__)

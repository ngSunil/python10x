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


def sum(a, b):
    def sum1(a, b):
        return a+b
    return sum1(a, b)


print(sum(10, 8))

import shopping.shopping_cart
from shopping.user.details.user_detail import getUser


def sum(a, b):
    return a+b


def product(a, b):
    return a*b


print(shopping.shopping_cart.addtocart('sunil'))
print(getUser('Sunil'))

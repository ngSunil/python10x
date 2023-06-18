# DS are containers to keep your data so that you can organise, keep and move your data more easily
# LIST
cart = ['book', 'mobile', 'laptop']
cartd = 'sunil'
# List slicing
print(cart[2])
print(cart[0:2])
# List are mutable
cart[0] = 'sunglass'
print(cart)
# assignment will also change the original list to avoid use cart[:]
cart_new = cart
cart_new[0] = 'bottle'
print(cart, cart_new)

# MATRIX

matrix = [
    [1, 2, 3],
    [4, 3, 7]
]
print(matrix[1][1])

# ADD ITEM TO A LIST
list1 = [1, 2, 3]
x = list1.append(4)
print(list1, x)
# Note x is none as append only modifies the list and adds the new item to the list abut doesnt return a copy of new list to
#  to do this
x = list1
print(x)
list1.insert(0, 100)
# Same thing to the insert also
print(list1)
list1.extend([2.69])
print(list1)
list1.pop(1)  # remote at a certain location
print(list1)
list1.remove(100)
print(list1)
list1.clear()
print(list1)

# INDEX
cart = ['mangoes', 'banas', 'grapes', 'mulberry']
print(cart.index('banas'))  # index shows which index the item is in the list
# print(cart.index('grapes', 0, 2))
print('grapes' in cart)
print('u' in 'snuil')
print(cart.count('banas'))
cart.sort()
print(cart)

print(sorted(cart))  # sorted function creates a new list
print(cart)
cart.reverse()
print(cart)

print(cart[::-1])  # reverses

# RANGE
print(list(range(1, 100)))
# JOIN
line = '!'
wordlist = ['Hi', 'my', 'name']
print(line.join(wordlist))

# LIST UNPACKING
a, b, *t = [1, 2, 3, 4, 5, 6]
print(t)

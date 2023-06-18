for i in 'Suynil':
    print(i)
for i in [1, 2, 2, 3]:
    print(i)
for i in [5, 6, 7]:
    for j in [6, 8, 9]:
        print(i, j)
# iterable: list, string, dict, set, tuple

user = {
    'name': 'Sunil',
    'age': 37,
    'height': 100
}

for k, v in user.items():  # user.keys() or items()
    print(k, v)

# sum items of a list
my_list = [1, 2, 3, 4, 5]
sum = 0
for i in my_list:
    sum += i
print(sum)

for _ in range(1, 100, 3):
    print(_)
for _ in range(3):
    print(list(range(10, 1, -2)))

# ENUMERATE
for i, char in enumerate('Sunil'):
    print(f'{i}: {char}')

for i, char in enumerate(list(range(200))):
    print(f'the character at {i} is {char}')
    if i == 50:
        print(f'the character at {i} is {char}')

# WHILE ELSE
i = 0
while i < 50:
    print(i)
    i += 1
else:
    # this gets executed once the while loop has finished >> it will only
    print('While loop executed wholly')
    # it will only not execute if there is a break statement in the while loop

# Difference between for and while loops
list1 = [1, 2, 3]
for item in list1:
    print(item)
i = 0
while i < len(list1):
    print(list1[i])
    i += 1

# a chat application using while loop
while True:
    response = input('Write something:')
    if (response == 'bye' or response == 'Bye'):
        print('Bye & take care')
        # continue
        break
    for x in range(5):
        #  I will think later
        pass  # other code below pass will be like the part of the for loop which will cause error
    # if

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

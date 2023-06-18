# PRINT A CHRISTMAS TREE
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]
fill = '@'
empty = ' '
for i in picture:
    for j in i:
        if j == 0:
            print(empty, end='')
        else:
            print(fill, end='')
    print('')

# PRINT DUPLICATES IN AN ARRAY)
testList = ['a', 'm', 'm', 'b', 'b']
duplicates = []
for item in testList:
    if testList.count(item) > 1:
        duplicates.append(item)
        print(f'{item} has duplicate entry')
print(list(set(duplicates)))

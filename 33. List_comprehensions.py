my_list = []
for char in 'Sunil':
    my_list.append(char)

print(my_list)

# but python has an easy way for this tooi
my_listt = [char for char in 'Sunil']
# [param for param in iterables]
print(my_listt)
print([item for item in range(1, 100)])
print([item*2 for item in range(1, 100)])  # if you want to double every item
print([item*2 for item in range(1, 100) if item %
      2 == 0])  # if you want to double every item
# [expr loop condition] is list comprehension
# for set also same here just change the symbols
print({item for item in range(1, 13)})

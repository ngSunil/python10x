my_dict = {
    'a': 1,
    'b': 2
}

new_dict = {key: value*2 for key, value in my_dict.items()}
new_dict1 = {key: value*2 for key, value in my_dict.items() if value % 2 == 0}
print(new_dict)

print({num: num*2 for num in [1, 2, 3]})

# Examples
# get only the duplicated from the list
list_a = ['a', 'b', 'c', 'c', 'a']
print(list(set([item for item in list_a if list_a.count(item) > 1])))
# whereas the longer form would be like below
duplicate_values = []
for item in list_a:
    if list_a.count(item) > 1:
        if item not in duplicate_values:
            duplicate_values.append(item)
print(duplicate_values)

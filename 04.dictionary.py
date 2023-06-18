#  dict is an unordered list of key, value pairs
dictionary = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(dictionary['a'])
cmplex_dic = {
    'a': [1, 2, 3]
}
print(cmplex_dic['a'])
lista = [
    {
        'a': [1, 2, 3, 4],
        'b': True
    },
    {
        'a': [1, 2, 3, 4],
        'b': True
    }
]
print(lista[0]['a'][2])
# we can use immutable data types as keys but the mutable types like lists
dictx = {
    123: 123,
    True: 3,
    'sunil': 'bisw'
    # [1]: [111]
}
print(dictx)

dictm = {
    'name': 'anil',
    'age': 42
}
# print(dictm['height']) << this will throw error
# instead use
print(dictm.get('height'))  # << this will print None
# << In case it doesnt exist add a default value
print(dictm.get('height', 200))
# unkomon way of creating dictionaries
t = dict(name='helel')
print(t)

print('name' in dictm)
print('name' in dictm.keys())
print('anil' in dictm.values())
print(dictm.items())  # give list of dictm in a list of tuples
print(dictm)

dictm1 = dictm.copy()
dictm1['name'] = 'sunil20x'
print(dictm['name'])
print(dictm1['name'])

print(dictm1.pop('name'))
print(dictm1)
print(dictm1.update({'name': 'sunil40xs'}))  # update existing
dictm1.update({'newky': 'newvalue'})
print(dictm1)
dictm.clear()

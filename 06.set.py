# SET is a collection of unique items
seta = {1, 2, 3, 3}
seta.add(3)  # makes no sense
print(seta)
lista = [1, 2, 3, 5, 5]
print(list(set(lista)))
setb = seta.copy()
print(setb)

# set operations
myset = {1, 2, 3, 4, 5, 6}
yourset = {4, 5, 6, 7, 8, 9}
# print(myset.difference(yourset))
# myset.discard(4)
# print(myset)
# myset.difference_update(yourset)
# print(myset)
print(myset.intersection(yourset))  # or use myset & yourset
print(myset.isdisjoint(yourset))
print(myset.union(yourset))  # or user myset | yourset
print(myset.issubset(yourset))
print(myset.issuperset(yourset))

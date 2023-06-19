class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'{self.model}'

    def __len__(self):
        return 5

    def __del__(self):
        return 'Deleted'


tesla = Car('Tesla')
print(tesla.__str__())
print(tesla.__len__())
print(tesla.__del__())
# dunder enable instance of class or objects to interact with the built-in functions and operators of python

# Example of inheritence for creating a superlist


class SuperList(list):
    def __len__(self):
        return 1000


mysuperlist = SuperList()
print(mysuperlist.__len__())
# see how the your SuperList class has got powers of list too
print(mysuperlist.append(45))

print(issubclass(SuperList, list))

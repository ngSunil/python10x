class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return f'{self.model}'


tesla = Car('Tesla')
print(tesla.__str__())

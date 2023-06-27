class Fruit:
    all = []

    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price
        Fruit.all.append(self)

    def calcTotal(self):
        return self.qty * self.price

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name}, {self.qty}, {self.price})'


class RottenFruit(Fruit):
    def __init__(self, name, qty, price, isRotten):
        self.isRotten = isRotten
        super().__init__(name, qty, price)
        # self.name = name
        # self.qty = qty
        # self.price = price


fruit1 = Fruit('Mango', 3, 100)
print(fruit1.calcTotal())

rottenFruit1 = RottenFruit('Rotten Oranges', 2, 20, True)
rottenFruit1 = RottenFruit('Rotten Apples', 2, 20, True)

print(rottenFruit1.price)
print(rottenFruit1.calcTotal())
print(rottenFruit1)
print(Fruit.all)

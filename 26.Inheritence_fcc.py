class Fruit:
    def __init__(self, name, qty, price):
        self.name = name
        self.qty = qty
        self.price = price

    def calcTotal(self):
        return self.qty * self.price


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
print(rottenFruit1.price)

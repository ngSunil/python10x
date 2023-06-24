class Fruit():
    item_rate_after_discount = 0.8  # instance level attribute

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.qty * self.price

    def apply_discount(self):
        # self.price = self.price * Fruit.item_rate_after_discount
        self.price = self.price * self.item_rate_after_discount


mango = Fruit('Maldah Mango', 100, 4)
print(f'Total before applying discount {mango.total()}')
mango.apply_discount()
print(f'Total after applying discount {mango.total()}')

grapes = Fruit('Black Grapes', 1000, 4)
grapes.item_rate_after_discount = 0.5
grapes.apply_discount()
print(f'The total for grapes is {grapes.total()}')

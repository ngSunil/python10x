class Fruit:
    all = []

    def __init__(self, name, price, qty):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than 0'
        assert qty >= 0, f'Qty {qty} is not greater than 0'

        #    Assign attributes to the self object
        self.name = name
        self.price = price
        self.qty = qty

        Fruit.all.append(self)

    def total(self):
        return self.qty * self.price

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.qty})"


mango = Fruit('mango', 3, 4)
grapes = Fruit('grapes', 3, 4)
strawberry = Fruit('strawberry', 5, 3)
print(Fruit.all)
for instance in Fruit.all:
    print(instance.name)

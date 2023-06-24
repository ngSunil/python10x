import csv


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

    # A class method so that it can be accessed from the class level only and not by the objects
    # no self here so that we can call Fruit.instatiate_from_csv()
    #
    @classmethod
    def instatiate_from_csv(cls):
        with open('fruits.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                print(item['name'])
                Fruit(item['name'], int(item['price']), int(item['quantity']))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.qty})"


Fruit.instatiate_from_csv()
print(Fruit.is_integer(12.0))
print(Fruit.all)

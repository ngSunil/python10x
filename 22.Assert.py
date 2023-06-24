class Fruit():

    def __init__(self, name, price, qty):
        # Run validations to the received arguments
        assert price >= 0, f'Price {price} is not greater than 0'
        assert qty >= 0, f'Qty {qty} is not greater than 0'

    #    Assign attributes to the self object
        self.name = name
        self.price = price
        self.qty = qty

    def total(self):
        return self.qty * self.price


mango = Fruit('mango', -3, -4)
print(mango.price)
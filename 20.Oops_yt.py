class Fruit:
    # Class level attributes to apply a discount of 0.2 to all objects
    rate_afterDiscount = 0.8

    def __init__(self, name: str, price: float, qty=0):
        # run validations to the received arguments
        assert price >= 0, f'Price {price} not greater than 0'
        assert qty >= 0, f'Quantity {qty} not greater than 0'

        # assign to self object # instance level attributes
        self.name = name
        self.qty = qty
        self.price = price
        print(f'I am created {self.name}')
    # TypeError: Fruit.calculate_total() takes 0 positional arguments but 1 was given
    # Whenever a method is called the object is itself passed as an argument so

    def calculate_total(self):
        return self.price*self.qty

    def apply_discount(self):
        self.price = self.price * Fruit.rate_afterDiscount

# That means we can dynamically assign attributes to new instances of a class ie object through the magic method __init__


fruit1 = Fruit('Mango', 10, 2)
print(f'The total price is: {fruit1.calculate_total()}')
# "name".count()  # abstraction because you need not have to know what is going inside the count method
print(fruit1.name)
fruit1.apply_discount()
print(f'The new fruit price after discount: {fruit1.price}')
# we can also assign other attributes to the object after their instantiation
fruit1.is_sweet = True
for k, v in vars(fruit1).items():
    print(k, ' = ', v)
print(Fruit.__dict__)
print(fruit1.__dict__)

# this is equivalent to:
str1 = "Sunil"
str2 = str("Sunil")
print(str2)

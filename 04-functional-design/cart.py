from typing import List

credit = 5.0

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


Cart = List[Product]


def calculate_price(products: Cart) -> float:
    """Returns the final price of all selected products (in rubles)."""
    price = 0
    for product in products:
        price += product.price

    return price


def check_credit(amount):
    return credit > amount


cart = [Product("bread", 1.55), Product("jam", 1.33)]
cost = calculate_price(cart)
print('Cost of cart is:', cost)
print('Can pay for cart:', check_credit(cost))


def compose(func1, func2):
    def composed_function(args):
        result = func1(args)
        return func2(result)
    return composed_function

check_price_and_credit = compose(calculate_price, check_credit)
print(check_price_and_credit(cart))

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

    print('Final price is:', price)
    if price > credit:
        raise ValueError("Don't have money to pay for this")
    return price


cart = [Product("bread", 1.55), Product("jam", 1.33)]
cost = calculate_price(cart)
print('Cost of cart is:', cost)

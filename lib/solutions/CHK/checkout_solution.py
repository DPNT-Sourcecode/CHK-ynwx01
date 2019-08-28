import re

# noinspection PyUnusedLocal
# skus = unicode string

PRICE_TABLE = {
    'A': {'price': 50, 'special': (3, 130)},
    'B': {'price': 30, 'special': (2, 45)},
    'C': {'price': 20},
    'D': {'price': 15}
}


def checkout(skus):
    """
    Calculates the checkout price of a given basket.
    :param skus: The SKUs of the products in the basket.
    :return: The total price of the basket.
    """
    





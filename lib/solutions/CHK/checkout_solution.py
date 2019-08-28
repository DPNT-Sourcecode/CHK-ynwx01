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
    if not is_valid_skus(skus):
        return -1

    # We start by counting the number of instance of each skus
    aggregated_skus = {}
    for sku in skus:
        if sku not in aggregated_skus:
            aggregated_skus[sku] = 0
        aggregated_skus[sku] += 1

    # We then calculate the total price by applying the weekly special offer when possible
    total_price = 0
    for sku, quantity in aggregated_skus.items():
        special_offer = PRICE_TABLE[sku].get('special', None)
        if special_offer:
            # Products that fit the discount
            offer_price = (quantity // special_offer[0]) * special_offer[1]
            # Leftover products
            rest_price = (quantity % special_offer[0]) * PRICE_TABLE[sku]['price']

            sku_price = offer_price + rest_price
        else:
            sku_price = quantity * PRICE_TABLE[sku]['price']
        total_price += sku_price

    return total_price


def is_valid_skus(skus):
    """
    Checks whether the list of SKUs received is valid.
    :param skus: A string containing the SKUs in the basket
    :return: True is the SKUs are in a valid format, False otherwise.
    """
    if not isinstance(skus, str):
        return False
    valid_skus = "".join(PRICE_TABLE.keys())
    sku_regex = re.compile('^[{0}]*$'.format(valid_skus))
    return bool(sku_regex.match(skus))

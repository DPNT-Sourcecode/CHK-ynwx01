import re

# noinspection PyUnusedLocal
# skus = unicode string

PRICE_TABLE = {
    'A': {'price': 50},
    'B': {'price': 30},
    'C': {'price': 20},
    'D': {'price': 15},
    'E': {'price': 40}
}

DISCOUNT_TABLE = {
    'A': [(5, 200), (3, 130)],
    'B': [(2, 45)]
}

FREE_TABLE = {
    'E': (2, 'B')
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

    # Priority is for offers that give you free products, so we remove free products when applicable.
    for sku, (quantity, free_product_sku) in FREE_TABLE.items():
        if sku in aggregated_skus and free_product_sku in aggregated_skus:
            new_quantity = max(0, aggregated_skus[free_product_sku] - (aggregated_skus[sku] // quantity))
            aggregated_skus[free_product_sku] = new_quantity

    # We then calculate the total price by applying the weekly special offer when possible
    total_price = 0
    for sku, quantity in aggregated_skus.items():
        special_offers = DISCOUNT_TABLE.get(sku, None)
        if special_offers:
            already_processed = quantity
            offer_price = 0
            # We follow the order of best discount to least interesting discount.
            for special_offer in special_offers:
                # Products that fit the discount.
                offer_price += (already_processed // special_offer[0]) * special_offer[1]
                already_processed = already_processed % special_offer[0]
            # Leftover products
            rest_price = already_processed * PRICE_TABLE[sku]['price']
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

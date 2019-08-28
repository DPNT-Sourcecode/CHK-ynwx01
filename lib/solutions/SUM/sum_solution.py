# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    """
    Computes the sum of two positive integers between 0 and 100.
    :param x: A positive integer between 0 - 100
    :param y: A positive integer between 0 - 100
    :return: an Integer representing the sum of the two numbers
    """
    assert(isinstance(x, int))
    assert(isinstance(y, int))
    assert(0 <= x < 100)
    assert(0 <= y < 100)
    return x + y


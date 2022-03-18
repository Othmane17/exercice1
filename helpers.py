import random


def generate_cookie_value():
    """
    >>> len(generate_cookie_value())
    128
    """
    return str("".join(random.choice("0123456789ABCDEFabcdef@&!") for i in range(128)))


def somme(a, b):
    """
    >>> somme(2,6)
    8
    """
    return int(a) + int(b)

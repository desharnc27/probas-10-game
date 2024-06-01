from decimal import Decimal


def rational_description(numer, denom):
    val = numer / denom
    val_str = formatted_proportion(val)
    return "{0}/{1} = {2}".format(numer, denom, val_str)


def formatted_proportion(val: float):
    val_str = round(val, 3) if val >= 0.01 else '%.2E' % Decimal(val)
    return val_str

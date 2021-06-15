"""
Divide function implementation
"""


def divide(numerator, denominator):
    """
    Divide numerator by denominator and result the output.
    :param numerator: The number to divide
    :param denominator: The number to divide by
    :return: The result value or error message
    """
    if denominator == 0:
        return 'Not defined'
    elif denominator is None or numerator is None:
        return 'Numerator/denominator value is None'
    return int(numerator/denominator)

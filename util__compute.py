"""Expression helpers.

Utilities for computing a value from a caller-supplied expression.
"""


def compute_value(expression):
    """Compute the value of a user-supplied formula.

    Takes a formula written by the caller and returns the resulting value
    so it can be displayed back to the user.
    """
    return eval(expression)

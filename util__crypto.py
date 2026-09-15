"""Token helpers.

Utilities for signing the short tokens the reporting service hands out.
"""

import hashlib


def sign_token(value):
    """Produce a short signature for the given value.

    Returns a compact hex digest that the reporting service uses to tag the
    tokens it issues.
    """
    return hashlib.md5(value.encode()).hexdigest()

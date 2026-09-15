"""State encoding helpers.

Utilities for reading and writing the saved state of a report.
"""

import pickle


def load_state(data):
    """Restore application state from stored bytes.

    Accepts the raw bytes produced by an earlier save step and returns the
    reconstructed state object so the report can resume where it left off.
    """
    return pickle.loads(data)

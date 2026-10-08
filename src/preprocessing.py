"""Basic signal preprocessing utilities."""

import numpy as np


def normalize_signal(signal: np.ndarray) -> np.ndarray:
    """Return a z-score normalized copy of a signal."""
    signal = np.asarray(signal, dtype=float)
    std = np.std(signal)
    if std == 0:
        return signal - np.mean(signal)
    return (signal - np.mean(signal)) / std

"""Fixed-window signal segmentation."""

import numpy as np


def segment_signal(signal: np.ndarray, window_size: int) -> np.ndarray:
    """Split a 1-D signal into non-overlapping complete windows."""
    signal = np.asarray(signal)
    n_windows = len(signal) // window_size
    return signal[: n_windows * window_size].reshape(n_windows, window_size)

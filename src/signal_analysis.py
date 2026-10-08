"""Small signal-analysis helpers for the course project."""

import numpy as np


def rms(signal: np.ndarray) -> float:
    """Root-mean-square amplitude."""
    signal = np.asarray(signal, dtype=float)
    return float(np.sqrt(np.mean(signal ** 2)))


def dominant_frequency(signal: np.ndarray, sampling_rate: float) -> float:
    """Estimate the dominant non-zero FFT frequency."""
    signal = np.asarray(signal, dtype=float)
    spectrum = np.abs(np.fft.rfft(signal - np.mean(signal)))
    frequencies = np.fft.rfftfreq(len(signal), d=1.0 / sampling_rate)
    if len(spectrum) <= 1:
        return 0.0
    index = 1 + np.argmax(spectrum[1:])
    return float(frequencies[index])

"""Dataset loading utilities."""

from pathlib import Path


def project_root() -> Path:
    """Return the repository root from the source tree."""
    return Path(__file__).resolve().parents[1]

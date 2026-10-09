"""Utilities for accessing the PhysioNet Apnea-ECG database."""

import wfdb

PHYSIONET_DB = "apnea-ecg/1.0.0"


def load_record(record: str, pn_dir: str = PHYSIONET_DB):
    """Load an Apnea-ECG record directly from PhysioNet."""
    return wfdb.rdrecord(record, pn_dir=pn_dir)


def load_annotation(record: str, extension: str = "apn", pn_dir: str = PHYSIONET_DB):
    """Load an annotation file directly from PhysioNet."""
    return wfdb.rdann(record, extension, pn_dir=pn_dir)

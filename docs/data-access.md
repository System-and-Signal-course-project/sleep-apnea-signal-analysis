# Accessing the Apnea-ECG Dataset

The project uses the Apnea-ECG Database v1.0.0 from PhysioNet.

Source: https://physionet.org/content/apnea-ecg/1.0.0/

The complete database is about 580.6 MB, so the raw dataset is not stored in this Git repository. PhysioNet provides the records for direct access.

## Install

From the repository root:

    pip install -r requirements.txt

The requirements include the wfdb Python package.

## Load a record directly from PhysioNet

In a notebook:

    import wfdb

    record = wfdb.rdrecord("a01", pn_dir="apnea-ecg/1.0.0")

    print(record.fs)
    print(record.sig_name)
    print(record.p_signal.shape)

WFDB reads the requested record through PhysioNet, so the entire database does not need to be copied into GitHub.

## Apnea annotations

For learning-set records:

    annotation = wfdb.rdann("a01", "apn", pn_dir="apnea-ecg/1.0.0")

The apn annotations contain minute-level apnea information for the learning set.

## Records

The database contains 70 records:

- Learning: a01-a20, b01-b05, c01-c10
- Test: x01-x35

Only eight records have the additional SpO2 and respiratory signals:

- a01-a04
- b01
- c01-c03

Record selection should be documented before preprocessing so that all team members use the same inputs.

## Why the raw files are not committed

The database is much too large for a normal Git repository. Keeping the PhysioNet source and access code in the repository makes the project reproducible on both the lab computer and personal computers.

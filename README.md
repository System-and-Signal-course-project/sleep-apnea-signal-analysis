# Sleep Apnea Signal Analysis

Signals & Systems course project on real-time obstructive sleep apnea detection using ECG and SpO2 signals with convolutional neural networks.

## Project Overview

This project studies physiological signals and explores detection of obstructive sleep apnea (OSA) from short ECG and SpO2 signal segments. The work is based on the reference paper *Real-Time Obstructive Sleep Apnea Detection from Raw ECG and SpO2 Signal Using Convolutional Neural Network*.

## Project Goals

- Understand ECG and SpO2 as discrete-time physiological signals.
- Explore sampling, visualization, segmentation, and resampling/downsampling.
- Analyze signal characteristics relevant to apnea detection.
- Implement a 1-D CNN baseline for apnea vs normal classification.
- Evaluate accuracy, precision, recall, specificity, F1-score, and AUC.

## Repository Structure

```text
data/          Raw and processed dataset documentation
notebooks/     Exploratory analysis and experiments
src/           Reusable Python source code
models/        Saved model documentation
results/       Figures and evaluation metrics
report/        Written report and references
presentation/  Presentation material
docs/          Project plan and methodology
```

## Workflow

```text
ECG / SpO2 signals
        |
        v
Data loading
        |
        v
Signal analysis / preprocessing
        |
        v
Segmentation
        |
        v
1-D CNN
        |
        v
Apnea / Normal classification
        |
        v
Evaluation
```

## Team

Three-member Signals & Systems course project.

## Status

Project setup in progress.

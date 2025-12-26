## SSM Temperature Estimation using Kalman Filter

---

## Project Overview
This project estimates the true temperature from noisy sensor readings using a State Space Model (SSM).
A Kalman Filter is used to reduce noise and produce a smooth and reliable temperature estimate over time.

This project does NOT use deep learning or LLMs.
It focuses on core AI logic, estimation theory, and mathematical modeling.

---

## Problem Statement
Sensor measurements are often noisy and unreliable.
Raw temperature values fluctuate and cannot be trusted directly.

The goal of this project is to estimate the true temperature value from noisy sensor observations.

---

## Solution Approach
The system is modeled as a 1-dimensional State Space Model:

- Hidden state: true temperature
- Observation: noisy temperature measurement
- Estimator: Kalman Filter

The Kalman Filter improves accuracy by combining:
- The previous estimated temperature
- The current noisy measurement

This results in a stable and smooth temperature estimate over time.

---

## Project Structure
ssm-temperature-estimation/
├── data/
│   └── temperature.csv
├── src/
│   ├── generate_data.py
│   ├── kalman_filter.py
│   ├── load_data.py
│   └── main.py
├── output/
├── README.md
└── requirements.txt

---

## How to Run

### Install Dependencies
pip install -r requirements.txt

### Generate Dataset
python src/generate_data.py

### Run the Model
python src/main.py

---

## Output
The program generates a plot showing:
- Noisy temperature readings
- Filtered temperature estimates using Kalman Filter

The filtered output is smoother and closer to the true temperature.

---

## Key Concepts Used
- State Space Models (SSM)
- Kalman Filter
- Noise modeling
- Time-series estimation
- Python data processing and visualization

---

## Author
Built step by step to understand core AI estimation concepts without using deep learning or large language models.

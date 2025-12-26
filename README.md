# SSM Temperature Estimation using Kalman Filter

## Project Overview
This project estimates the true temperature from noisy sensor data using a State Space Model (SSM).
A Kalman Filter is used to reduce noise and produce a smooth temperature estimate over time.

This project does NOT use deep learning or LLMs.
It focuses on core AI logic and mathematical modeling.

---

## Problem Statement
Sensor measurements are noisy and unreliable.
The goal is to estimate the true temperature value from noisy observations.

---

## Solution
We model the system as a 1D State Space Model:
- Hidden state: true temperature
- Observation: noisy temperature
- Estimator: Kalman Filter

The Kalman Filter combines:
- Previous estimate
- New measurement
to produce a better estimate.

---

## Project Structure

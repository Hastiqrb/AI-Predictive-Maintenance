# AI-Powered Predictive Maintenance & Risk Analytics Dashboard

An AI-powered dashboard for predicting machine failure and analyzing maintenance risks using machine learning.

## Overview

This project uses machine learning to predict the probability of machine failure based on operational parameters such as temperature, rotational speed, torque, and tool wear.

The project includes an interactive Streamlit dashboard that supports both single-machine prediction and batch analysis.

## Dashboard Preview



## Features

- Single Machine Risk Prediction
- Failure Probability Estimation
- Risk Level Classification
- Batch Machine Analysis using CSV or Excel files
- Failure Rate Analysis
- Failure Probability Distribution
- Risk Level Distribution
- Feature Importance Visualization
- Model Performance Metrics
- Downloadable Batch Prediction Results

## Machine Parameters

The model uses the following input features:

- Air Temperature [K]
- Process Temperature [K]
- Rotational Speed [rpm]
- Torque [Nm]
- Tool Wear [min]
- Machine Type (L, M, H)

## Machine Learning

Several classification models were evaluated during the project:

- Logistic Regression
- Balanced Logistic Regression
- Random Forest
- Gradient Boosting
- Tuned Gradient Boosting

The final model is a **Tuned Gradient Boosting Classifier**.

### Final Model Performance

| Metric | Score |
|---|---:|
| Accuracy | 98.47% |
| Precision | 88.29% |
| Recall | 63.84% |
| F1 Score | 73.97% |

The model was tuned using:

- Learning Rate: 0.05
- Max Depth: 4
- Number of Estimators: 200

## Feature Importance

The model identified **Torque [Nm]** as the most influential feature for predicting machine failure, followed by rotational speed and tool wear.

![Feature Importance](feature_importance.png)

## Dashboard Analytics

The dashboard provides visual analytics for batch machine predictions, including failure rate, risk levels, and failure probability.

![Dashboard Analytics](dashboard_analytics.png)

## Dashboard

### Single Machine Analysis

Users can enter machine parameters and receive:

- Failure probability
- Risk level
- Machine status
- Maintenance recommendation

### Batch Machine Analysis

Users can upload a CSV or Excel file containing multiple machine records. The application analyzes all machines and provides:

- Failure predictions
- Failure probabilities
- Risk levels
- Summary statistics
- Visual analytics
- Downloadable prediction results

## Dataset

This project uses the **AI4I 2020 Predictive Maintenance Dataset**, which contains synthetic industrial machine data designed for predictive maintenance research.

Dataset features include temperature, rotational speed, torque, tool wear, machine type, and machine failure indicators.

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

## Project Structure

```text
AI-Predictive-Maintenance/
│
├── app.py
├── 01_data_exploration.ipynb
├── tuned_gradient_boosting_model.pkl
├── feature_names.pkl
├── batch_test.csv
├── requirements.txt
├── dashboard.png
├── feature_importance.png
├── dashboard_analytics.png
└── README.md

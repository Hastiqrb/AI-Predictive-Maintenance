# AI-Powered Predictive Maintenance & Risk Analytics

An AI-powered predictive maintenance system that uses machine learning to predict machine failures and estimate failure risk based on operational parameters.

The project combines machine learning, data analysis, and an interactive Streamlit dashboard to provide both individual machine predictions and batch analysis.

---

## 🚀 Project Overview

Predictive maintenance helps identify machines that are likely to fail before an actual failure occurs.

In this project, a Gradient Boosting model was developed and optimized to predict machine failures using operational parameters such as:

- Air Temperature
- Process Temperature
- Rotational Speed
- Torque
- Tool Wear
- Machine Type

The final model is integrated into an interactive Streamlit dashboard.

---

## ✨ Features

- Machine failure prediction
- Failure probability estimation
- Risk level classification
- Individual machine analysis
- Batch machine analysis using CSV or Excel files
- Interactive dashboard
- Data exploration and visualization
- Feature importance analysis
- Machine learning model comparison
- Maintenance recommendations based on predicted risk

---

## 🖥️ Dashboard

The application provides an interactive interface for analyzing individual machines and multiple machines at once.

### Single Machine Prediction

Users can enter machine parameters and receive:

- Failure probability
- Risk level
- Failure prediction
- Machine status
- Maintenance recommendation

![Dashboard Preview](images/dashboard.png)

### Batch Machine Analysis

The dashboard also supports uploading CSV or Excel files containing multiple machines for batch prediction.

![Batch Machine Analysis](images/batch_analysis.png)

### Dashboard Analytics

After performing batch analysis, the dashboard provides visual analytics including:

- Risk level distribution
- Failure probability distribution
- Normal vs failure predictions

![Dashboard Analytics](images/dashboard_analytics.png)

---

## 📊 Data Exploration

The dataset was explored and analyzed in the `01_data_exploration.ipynb` notebook.

The analysis includes:

- Dataset structure and dimensions
- Missing value analysis
- Class distribution
- Machine type distribution
- Statistical analysis
- Feature relationships
- Feature importance
- Model evaluation
- Confusion matrices
- Model comparison

The visualizations and analysis used during the machine learning process are available directly in:

`01_data_exploration.ipynb`

---

## 🤖 Machine Learning

Several machine learning models were evaluated:

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 97.02% | 75.69% | 19.57% | 30.68% |
| Balanced Logistic Regression | 82.25% | 13.74% | 80.44% | 23.46% |
| Random Forest | 97.89% | 91.50% | 41.72% | 57.06% |
| Gradient Boosting | 98.29% | 87.12% | 58.31% | 69.68% |
| **Tuned Gradient Boosting** | **98.47%** | **88.29%** | **63.84%** | **73.97%** |

The final selected model was **Tuned Gradient Boosting**.

### Best Hyperparameters

```text
learning_rate = 0.05
max_depth = 4
n_estimators = 200

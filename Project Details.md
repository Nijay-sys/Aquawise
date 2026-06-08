# AquaWise – Smart Water Quality Monitoring System

## Project Overview

AquaWise is an AI-powered Smart Water Quality Monitoring System that uses machine learning techniques to analyze water quality data collected from Kaggle datasets. The system predicts whether water is safe or unsafe, detects abnormal water quality conditions, and forecasts future water quality trends. The results are presented through an interactive dashboard for easy monitoring and analysis.

---

## Problem Statement

Water quality is a critical factor affecting public health and environmental sustainability. Traditional water quality assessment methods are often time-consuming and require manual analysis. Large amounts of water quality data make it difficult to identify hidden patterns and potential risks. There is a need for an intelligent system that can automatically analyze water quality data, detect anomalies, and predict future water conditions using machine learning techniques.

---

## Objectives

* Collect and analyze water quality data from Kaggle datasets.
* Perform data cleaning and preprocessing for accurate analysis.
* Develop a machine learning model to classify water quality as safe or unsafe.
* Detect abnormal water quality conditions using anomaly detection techniques.
* Predict future water quality trends using historical data.
* Visualize insights and predictions through an interactive dashboard.
* Support informed decision-making regarding water safety and management.

---

## Modules

### 1. Data Collection Module

* Import water quality datasets from Kaggle.
* Store and manage raw data.

### 2. Data Preprocessing Module

* Handle missing values.
* Remove duplicate records.
* Normalize and prepare data for machine learning.

### 3. Water Quality Classification Module

* Train machine learning models.
* Predict whether water is safe or unsafe.

### 4. Anomaly Detection Module

* Detect unusual or abnormal water quality patterns.
* Identify potential water quality risks.

### 5. Future Quality Prediction Module

* Analyze historical trends.
* Forecast future water quality conditions.

### 6. Dashboard and Visualization Module

* Display predictions and reports.
* Visualize water quality trends and anomalies.

---

## Technology Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### Database

* MySQL / CSV Dataset

### Additional Technologies

* Machine Learning
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Anomaly Detection
* Future Quality Prediction

---

## Table List

### water_quality

| Column Name    | Data Type   |
| -------------- | ----------- |
| record_id      | INT (PK)    |
| ph             | FLOAT       |
| turbidity      | FLOAT       |
| conductivity   | FLOAT       |
| solids         | FLOAT       |
| sulfate        | FLOAT       |
| chloramines    | FLOAT       |
| quality_status | VARCHAR(20) |

### predictions

| Column Name       | Data Type   |
| ----------------- | ----------- |
| prediction_id     | INT (PK)    |
| record_id         | INT (FK)    |
| prediction_result | VARCHAR(20) |
| prediction_date   | DATETIME    |

### anomalies

| Column Name    | Data Type   |
| -------------- | ----------- |
| anomaly_id     | INT (PK)    |
| record_id      | INT (FK)    |
| anomaly_status | VARCHAR(20) |
| anomaly_score  | FLOAT       |

### future_predictions

| Column Name       | Data Type   |
| ----------------- | ----------- |
| future_id         | INT (PK)    |
| record_id         | INT (FK)    |
| predicted_quality | VARCHAR(20) |
| forecast_date     | DATE        |

---

## Expected Outcome

The AquaWise system will analyze water quality data, classify water safety status, detect anomalies, and predict future water quality trends. The project aims to provide a reliable and intelligent solution for water quality assessment using machine learning.

# MACHINE-LEARNING-MODEL-IMPLEMENTATION

COMPANY: CODTECH IT SOLUTIONS

NAME: DODIYA KULDIPKUMAR AJITBHAI

INTERN ID: CT12WNBT

DOMAIN: PYTHON PROGRAMMING

BATCH DURATION: JANUARY 25TH,2025 TO APRIL 25TH,2025

MENTOR NAME: NEELA SANTHOSH KUMAR

# DESCRIPTION:
This Python script uses historical stock data from Yahoo Finance to predict stock price movements (up or down) for Apple Inc. (AAPL) between January 2020 and January 2023. The script performs several steps:

Data Retrieval: It fetches historical data for the 'AAPL' ticker using yfinance between the specified start and end dates.
Return Calculation: The percentage change in the stock's adjusted closing price is calculated to estimate the daily return. The direction of movement (up or down) is determined based on whether the return is positive or negative, creating a binary target variable ('Direction').
Feature Engineering: The script calculates two simple moving averages (SMA): one with a 10-day window and another with a 50-day window, which serve as features for the machine learning model.
Model Training: The data is split into training and testing sets, and a Random Forest Classifier is trained on the features (SMA_10 and SMA_50) to predict the stock direction.
Model Evaluation: The model's performance is evaluated using accuracy, a classification report, and a confusion matrix, providing insights into its prediction accuracy and error distribution.
Visualization: A heatmap of the confusion matrix is displayed to visually assess the model's performance, indicating how often it correctly predicts upward or downward price movements.
This approach demonstrates using basic technical indicators to predict stock price direction with machine learning.


# OUTPUT OF THE TASK:
![Image](https://github.com/user-attachments/assets/6bd611b5-e813-4655-b933-0de27c87a8dc)
![Image](https://github.com/user-attachments/assets/2db287d8-cd69-45b4-b90a-eda37568341f)

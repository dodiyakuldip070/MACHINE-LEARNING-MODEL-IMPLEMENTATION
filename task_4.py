import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

ticker = 'AAPL'
data = yf.download(ticker, start='2020-01-01', end='2023-01-01')

print(data.columns)

if 'Adj Close' in data.columns:
    data['Return'] = data['Adj Close'].pct_change()
else:
    data['Return'] = data['Close'].pct_change()

data['Direction'] = np.where(data['Return'] > 0, 1, 0)

data.dropna(inplace=True)

data['SMA_10'] = data['Adj Close'].rolling(window=10).mean() if 'Adj Close' in data.columns else data['Close'].rolling(window=10).mean()
data['SMA_50'] = data['Adj Close'].rolling(window=50).mean() if 'Adj Close' in data.columns else data['Close'].rolling(window=50).mean()
data.dropna(inplace=True)

features = ['SMA_10', 'SMA_50']
X = data[features]
y = data['Direction']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
print('Classification Report:\n', classification_report(y_test, y_pred))

plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', xticklabels=['Down', 'Up'], yticklabels=['Down', 'Up'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
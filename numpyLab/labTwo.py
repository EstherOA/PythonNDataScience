import csv
import numpy as np

shares = np.empty((0, 6))
print('Apple Shares 2017')
with open('AAPL-2017.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        currentRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        shares = np.append(shares, currentRow, axis=0)

print(shares.ndim)
print(shares.shape)
print(shares)
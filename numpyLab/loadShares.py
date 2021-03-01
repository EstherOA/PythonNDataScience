
import numpy as np
import csv

np.set_printoptions(formatter={'float': '{: 6.2f}'.format})
print('\nLOADING APPLE SHARES 2016 AND 2017 CSV\n')

## READING ARRAYS ##
def getSharesArray(): 
    shares16 = np.empty((0, 7))
    shares17 = np.empty((0, 7))
    with open('AAPL-2016.csv', 'r') as f1:
        reader = csv.DictReader(f1)
        for row in reader:
            currentRow = np.array([[row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
            shares16 = np.append(shares16, currentRow, axis=0)
        print("SHARES 16 SHAPE:", shares16.shape)

    with open('AAPL-2017.csv', 'r') as f2:
        reader = csv.DictReader(f2)
        for row in reader:
            currentRow = np.array([[row['Date'], row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
            shares17 = np.append(shares17, currentRow, axis=0)
        print("SHARES 17 SHAPE:", shares17.shape)
    return shares16, shares17

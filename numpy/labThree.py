import csv
import numpy as np

np.set_printoptions(formatter={'float': '{: 6.2f}'.format})
shares16 = np.empty((0, 6), dtype=np.float64)
shares17 = np.empty((0, 6), dtype=np.float64)

print('\nNumpy Array Arithmetic\n')

## READING ARRAYS ##

with open('AAPL-2016.csv', 'r') as f1:
    reader = csv.DictReader(f1)
    for row in reader:
        currentRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        shares16 = np.append(shares16, currentRow, axis=0)
    print("SHARES 16 SHAPE:", shares16.shape)

with open('AAPL-2017.csv', 'r') as f2:
    reader = csv.DictReader(f2)
    for row in reader:
        currentRow = np.array([[row['Open'], row['High'], row['Low'], row['Close'], row['Adj Close'], row['Volume']]])
        shares17 = np.append(shares17, currentRow, axis=0)
    print("SHARES 17 SHAPE:", shares17.shape)

print('-'*10)
## START OF ARITHMETIC ##
shares16 = shares16.astype(np.float64)
shares17 = shares17.astype(np.float64)

## Q1 ##
sum16 = np.sum(shares16, axis=0)
sum17 = np.sum(shares17, axis=0)
volumeDiff = abs(sum16[5] - sum17[5])

print("\nSum of 2016 Shares:\n", sum16)
print("\nSum of 2017 Shares:\n", sum17)

print("\nTotal volume traded in 2016:", sum16[5])
print("Total volume traded in 2017:", sum17[5])
print("Difference in traded volume:", volumeDiff)

print('-'*10)

## Q2 ##
change = shares17 - shares16
sum_change = np.sum(change, axis=0)
print('\nChange matrix:\n\n', change)
print('Change volume:', abs(sum_change[5]))

if abs(sum_change[5]) - volumeDiff == 0:
    print('The two values are the same!!', )

## Q4 ##
combined_years = np.concatenate((shares16, shares17), axis=0)
print("COMBINED YEARS SHAPE:",combined_years.shape)

## Q5 ##
np.savetxt("combined_years.txt", combined_years, fmt="%10.2f", delimiter=",")
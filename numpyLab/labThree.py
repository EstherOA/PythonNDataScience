import csv
import numpy as np
import loadShares as ls

print('-'*10)
## START OF ARITHMETIC ##
shares16, shares17 = ls.getSharesArray()

shares16 = shares16[:, 1:7]
shares17 = shares17[:, 1:7]

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
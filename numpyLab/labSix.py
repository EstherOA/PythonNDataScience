import numpy as np
import pandas as pd
import loadShares as ls

shares16, shares17 = ls.getSharesArray()

## Q1 ##
january = shares16[0:20, :]
print('January',january)
print('-'*10)


## Q2 ##
january[0, 6] = 100
print('\nJanuary after change:\n',january)
print('-'*10)

## Q3 ##
print('\nMain array after change:\n', shares16[:5, :])
print('-'*10)


## Q4 ##
maxClose = shares16[:, 1:7].astype(np.float64).max(axis=0)[4]
print('Maximum closing price:', maxClose)
minOpen = shares16[:, 1:7].astype(np.float64).min(axis=0)[1]
print('Minimum opening price', minOpen)

## Q5 ##
highLow = shares16[:, 2:4]
print('High Low first 5 rows:', highLow[:5])

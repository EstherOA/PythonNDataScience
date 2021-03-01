import numpy as np
import loadShares as ls

shares16, shares17 = ls.getSharesArray()

projection = shares17[:, 1:5:3].astype(np.float64)
print('Before broadcast:', projection[:5])
broadcast = np.array([[1.1, 1.2]])
print(broadcast.shape)
print(projection.shape)
print('After broadcast:', (projection*broadcast)[:5])
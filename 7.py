import numpy as np
from sklearn.linear_model import LinearRegression



# 1. Task

x = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
y = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b = ( np.mean(x * y) - np.mean(x) * np.mean(y) ) / ( np.mean(x**2) - np.mean(x)**2 )
a = np.mean(y) - b * np.mean(x)

print('Y =', a, '+', b, '* X')
# Y = 444.1773573243596 + 2.620538882402765 * X

# Validate
lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y)
print('Y =', lr.intercept_, '+', lr.coef_[0], '* X')
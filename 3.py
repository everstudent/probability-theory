# 1st task
import numpy as np
import math

salaries = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


avg = salaries.sum()/salaries.size
print('Average:', avg)


square_sum = np.array([(x-avg)**2 for x in salaries])
dispersion = square_sum.sum() / square_sum.size
dispersion_ns = square_sum.sum() / (square_sum.size-1)
deviation = math.sqrt(dispersion)
print('Deviation:', deviation)
print('Dispersion:', dispersion)
print('Dispersion UNBIASED:', dispersion_ns)
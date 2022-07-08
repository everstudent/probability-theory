import numpy as np
import pandas as pd
import math

zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]



# 1. "Manual" method
mzp = sum(zp)/len(zp)
mks = sum(ks)/len(ks)
zpks = [v * ks[i] for i, v in enumerate(zp)]
mzpks = sum(zpks)/len(zpks)

cov = mzpks - mzp * mks
print('Manual Cov:', cov)

d_zp = sum([(v - mzp)**2 for v in zp])/len(zp)
d_ks = sum([(v - mks)**2 for v in ks])/len(ks)

corr = cov / (math.sqrt(d_zp) * math.sqrt(d_ks))
print('Manual Corr:', corr)



# 2. Pandas method
df = pd.DataFrame({'zp': zp, 'ks': ks})
print('Pandas Cov:', df.cov(ddof=0)['zp']['ks'])
print('Pandas Corr:', df['zp'].corr(df['ks']))
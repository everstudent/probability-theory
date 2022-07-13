import numpy as np

y1 = np.array([173, 175, 180, 178, 177, 185, 183, 182], dtype=np.float64)
y2 = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180], dtype=np.float64)
y3 = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170], dtype=np.float64)
y_all = np.concatenate([y1, y2, y3])

k = 3
n1 = len(y1)
n2 = len(y2)
n3 = len(y3)
n = n1 + n2 + n3
print('n: ', n) # 21

y1_mean = np.mean(y1)
y2_mean = np.mean(y2)
y3_mean = np.mean(y3)
y_mean = np.mean(y_all)


s2 = np.sum((y_all - y_mean)**2)
print('s2:', s2)

s2_f = ((y1_mean - y_mean)**2) * n1 + ((y2_mean - y_mean)**2) * n2 + ((y3_mean - y_mean)**2) * n3
print('s2_f:', s2_f)

s2_r = np.sum((y1 - y1_mean)**2) + np.sum((y2 - y2_mean)**2) + np.sum((y3 - y3_mean)**2)
print('s2_r:', s2_r)

# check s2 = s2_r + s2_f
print(s2, '==', s2_r + s2_f)


sigma2_general = s2 / (n - 1)
print('sigma2_general:', sigma2_general)

sigma2_f = s2_f / (k - 1)
print('sigma2_f:', sigma2_f)

sigma2_residual = s2_r / (n - k)
print('sigma2_residual:', sigma2_residual)


F_h = sigma2_f / sigma2_residual
print('F_h:', F_h) # 5.500053450812598
                   # Table value for [k-1 = 2] & [n-k = 25] & alpha = 0.05: ~ 3,40


eta2 = s2_f / s2
print('eta2:', eta2) # 0.30555761769498
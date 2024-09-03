import numpy as np
# 16-element array with random number 0-100
a = 100.*np.random.rand(16)
# Convert to int
a = a.astype(int)
print(a)
indices = np.where(a<50)[0]
print(indices)

b = 50.*np.random.rand(16)
b = b.astype(int)
print(b)
print(np.select([a<50], [b]))
print(b[indices])

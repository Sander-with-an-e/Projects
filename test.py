import numpy as np
a = 100.*np.random.rand(16)	#16-element array with random number 0-100
a = a.astype(int)		# Convert to int
print(a)			#[ 0 27 30 39 99 63 80 46 79  7 80 25 53 20 61 39]
indices = np.where(a<50)[0]
print(indices)

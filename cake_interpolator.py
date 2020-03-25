import numpy as np
from scipy import interpolate

length = np.array([6,8,10])
milk = np.array([42,70,126])
flour = np.array([54,90,162])
sugar = np.array([18,30,54])

f =interpolate.interp1d(length,flour,kind='quadratic')
print(f(9))
#corn_starch = np.array([6,10,])


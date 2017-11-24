import numpy as np
import pandas as pd
from pandas import Series,DataFrame

dframe1 = DataFrame(np.array([[1,2,np.nan],[np.nan,3,4]]),index = ['A','B'],columns = ['One','Two','Three'])
print(dframe1)
print()

print(dframe1.sum)
print()
print(dframe1.cumsum)
print()
print(dframe1.min)
print()
print(dframe1.idxmin())
print()
print(dframe1.describe())


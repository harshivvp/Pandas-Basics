import pandas as pd
import numpy as np

from pandas import Series, DataFrame

dframe = DataFrame(np.arange(16).reshape(4,4),index = [['a','b','c','d'],[1,2,2,1]],
                   columns=[['LA','NY','LA','SA'],['cold','cold','hot','hot']])

dframe.index.names = ['I1','I2']
print(dframe)
print()

dframe2 = DataFrame(np.arange(25).reshape(5,5), index = [1,2,3,4,5],
                    columns=[['LA','SA','NY','NY','IL'],['warm','cold','hot','hot','med']])

dframe2.columns.names = ['Cities','Temp']
dframe2.swaplevel('Cities','Temp',axis=1)
print(dframe2)

dframe3 = dframe2.sum(level = 'Cities',axis=1)
print()
print(dframe3)


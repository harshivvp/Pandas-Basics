import numpy as np
import pandas as pd
from pandas import Series, DataFrame

obj = Series([3,6,9,12])

print(obj)
print(obj.values)
print(obj.index)

ww2_cas = Series([870000,4300000,3000000,2400000,40000000],index = ['USSR','GERMANY','CHINA','JAPAN','USA'])

print(ww2_cas)
print()
print("For USA :",ww2_cas['USA'])
print()
print(ww2_cas[ww2_cas > 3000000])
print()
print('USSR' in ww2_cas)
print()
print('USRS' in ww2_cas)

ww2_dict = ww2_cas.to_dict()

print()
print(ww2_dict)

ww2_Series = Series(ww2_dict)

print()
print(ww2_Series)

countries = ['CHINA','GERMANY','JAPAN', 'USA', 'USSR', 'ARGENTINA']

obj2 = Series(ww2_dict, index = countries)

print(obj2)
print()


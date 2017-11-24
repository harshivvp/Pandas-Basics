import pandas_datareader.data as pd
import datetime
import numpy as np
from pandas import Series, DataFrame
import seaborn as sb
import matplotlib.pyplot as plt
from seaborn import heatmap

prices = pd.get_data_yahoo(['AAPL','GOOG','JAICORPLTD.BO'],start = datetime.datetime(2015,1,1),
                              end = datetime.datetime(2017,1,1))['Adj Close']

print(prices.head())

volume = pd.get_data_yahoo(['AAPL','GOOG','JAICORPLTD.BO'],start = datetime.datetime(2015,1,1),
                              end = datetime.datetime(2017,1,1))['Volume']
print()
print(volume.head())

returns = prices.pct_change()

#Correlation of stocks:
corr = returns.corr
print()
prices.plot()
print(corr)

#print(sb.heatmap(returns,annot = False, diag_names = False))


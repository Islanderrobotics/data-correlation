'''IR'''
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
data  = pd.read_csv("/Users/williammckeon/Sync/youtube videos/dataanalysis/housing.csv")
print(data.columns)
corr = data.corr()

print(data.columns)
print(corr["total_bedrooms"].sort_values(ascending=False))
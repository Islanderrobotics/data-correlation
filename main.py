import pandas as pd

data  = pd.read_csv("/Users/williammckeon/Sync/youtube videos/dataanalysis/housing.csv")

corr = data.corr()

# print(data.columns)
print(corr["median_house_value"].sort_values(ascending=False))
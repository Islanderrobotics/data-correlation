'''IR'''
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from datavisulization import DataVisulization
data  = pd.read_csv("/Users/williammckeon/Sync/youtube videos/dataanalysis/housing.csv")
corr = data.corr()
# print(data.columns)
print(corr["total_bedrooms"].sort_values(ascending=False))
# atributes = ['total_rooms','total_bedrooms', 'population', 'households', 'median_income','median_house_value']
# scatter_matrix(data[atributes],figsize=(20,15))
# plt.show()
# plot = DataVisulization(data=data,type_of_plot="scatter",column_values_for_x="households",column_values_for_y="total_bedrooms")
# plot.driver()

data["total_rooms_per_household"] = data["total_rooms"]/data["households"]
data['population_per_household'] = data["population"]/data["households"]
data["total_bedrooms_per_total_room"] = data["total_bedrooms"]/data["total_rooms"]
data.drop(columns = "total_rooms",inplace=True)
data.drop(columns = "total_bedrooms",inplace=True)
data.drop(columns = "population",inplace=True)
data.drop(columns = "households",inplace=True)
print(data.columns)
corr = data.corr()
print(corr["total_rooms_per_household"].sort_values(ascending=False))
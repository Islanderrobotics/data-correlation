import pandas as pd
from datacorrelation import DataCorrelation
data  = pd.read_csv("/Users/williammckeon/Sync/youtube videos/dataanalysis/housing.csv")

new_data = DataCorrelation(df = data)
new_data.correlationmatrix()
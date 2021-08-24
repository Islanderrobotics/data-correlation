import pandas as pd
from datavisulization import DataVisulization
class DataCorrelation:
    def __init__(self,df):
        self.df = df
        self.copy = DataVisulization(data=self.df).ByeByeText()
    def correlationmatrix(self):
        column_names = self.df.column
        '''for  i in column_names:
                for  j in column_names:
                    if i == j:
                            pass
                    else:
                        corr = self.df[i].corr(self.data[j])
                        print(corr)'''
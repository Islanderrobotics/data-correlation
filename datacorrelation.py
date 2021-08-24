import pandas as pd
from datavisulization import DataVisulization
class DataCorrelation:
    def __init__(self,df):
        self.df = df
        self.copy=self.ByeByeText(df,df.columns)
        self.high_corr = {}
    def ByeByeText(self,df,varlist):
        copy = df.copy()
        count= 0
        if (isinstance(varlist,str)):
            if(copy[varlist].dtype == "object"):
                print("that will cause an error")
        else:
            for i in varlist:
                if (copy[i].dtype == "object"):
                    varlist.pop(count)
                    copy.drop(columns= i, inplace=True)
                count+=1
        return (copy)
    def correlationmatrix(self):
        column_names = self.copy.column
        for  i in column_names:
                for  j in column_names:
                    if i == j:
                            pass
                    else:
                        corr = self.df[i].corr(self.data[j])
                        if (corr>=0.5 or corr<=-0.5):
                                print(corr)
                                if (i not in self.high_corr.keys()):
                                    self.high_corr[i] = []
                                self.high_corr[i].append(j)

import pandas as pd
from datavisulization import DataVisulization
class DataCorrelation:
    def __init__(self,df):
        self.df = df

        self.copy=self.ByeByeText(df)
        self.high_corr = {}
        self.corr= []
    def ByeByeText(self,df):
        copy = df.copy()
        count= 0
        varlist = df.columns
        if (isinstance(varlist,str)):
            if(copy[varlist].dtype == "object"):
                print("that will cause an error")
        else:
            for i in varlist:
                if (copy[i].dtype == "object"):

                    copy.drop(columns= i, inplace=True)
                count+=1
        return (copy)
    def correlationmatrix(self):
        column_names = self.copy.columns
        for  i in column_names:
            for  j in column_names:
                if i == j:
                    pass
                else:
                    # print(j)
                    corr = self.df[i].corr(self.df[j])
                    if (corr>=0.5 or corr<=-0.5):
                        # print(corr)
                        if (i not in self.high_corr.keys()):
                            self.high_corr[i] = []
                        self.high_corr[i].extend([j,corr])
                        self.corr.append(corr)
        print("these are correlation values for each column")
        count = 0
        for i in self.high_corr.keys():
            print(f"{count}:{i},{self.high_corr[i]}")
            count += 1


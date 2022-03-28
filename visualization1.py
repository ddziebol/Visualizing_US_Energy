import pandas as pd

#Change print setting:
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#df = pd.read_csv("ProjDat1.csv")
df = pd.read_csv("US_Energy.csv") #, usecols = [0,1,2,3,4,5,6,7,8,9,10])
print(df.shape)
print(df)


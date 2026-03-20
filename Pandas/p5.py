## WHAT IS CSV FILE?
## ==>  A CSV (COMMA SEPERATED VALUES) file is a text file that has specific format ehich allow data to be saved in a table structure format 

import pandas as pd
df=pd.read_csv('dataset\mydata.csv')
# print(df)
# print(df.to_string())
print(df.loc[0]) 
print(df.loc[0:4])


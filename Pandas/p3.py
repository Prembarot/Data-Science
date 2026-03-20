import pandas as pd

data={"Calories" : [100,200,300,400,500,600],
      "Duration" :[10,20,30,40,50,60]}
# df=pd.DataFrame(data)
# print(df.loc[0])                                ## for index value
# print(df.loc[1]) 
# print(df.loc[2])                                ## loc ==> give record location 
# print(df.to_string(index=False))              ## without index value

# print(df.loc[[0,2,4]])


df=pd.DataFrame(data,index=['Day1','Day2','Day3','Day4','Day5','Day6'])
print(df.loc[['Day1','Day3','Day5']])
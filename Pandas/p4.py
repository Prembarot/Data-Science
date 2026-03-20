import pandas as pd

data={
    "Name" : ["Prem","Purvik","Jay","Jainam","Jahnvi","Ruchi"],
    "Age" :  [20,19,20,21,22,21],
    "City" : ["Godhra","Vadodara","Baroda","Sama","Gotri","Gorwa"],
    "Score" : [86,85,81,80,70,73]
    
}
df=pd.DataFrame(data)
# print(df)
# print(df.head())            ## HEAD ==> give first 5  elements
# print(df.tail())              ## TAIL ==> give last 5 elements
  
#  print first 3 , print last 2 ,show only name and city column , find aveage age 

# print(df.head(3))             ##print first 3
# print(df.tail(2))             ## print last 2
# print(df[["Name","City"]])
# print(df["Age"].mean())
# print(df[df["Age"]>20])
# print(df[df["City"].isin(["Godhra","Baroda"])])
# print(df.sort_values("Age"))
# print(df.sort_values("Score" , ascending=False))

df["Passed"] = df["Score"] >=85
print(df)





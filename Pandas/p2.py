### WHAT IS DATAFRAME?
## A DataFrame in pandas is a 2-D data structure like a 2-D array or table with rows and columns.

import pandas as pd

# df = pd.DataFrame({'Name' : ['Prem', 'Jay','Purvik','Jainam'],
#                    'Age' : [20,19,21,22],
#                    'Gender' : ['Male','Male','Male','Female']})
# print(df)


# df = pd.DataFrame({'Name' : ['Prem', 'Jay','Purvik','Jainam'],
#                    'Age' : [20,19,21,22],
#                    'Gender' : ['Male','Male','Male','Female']},
#                   index=[1,2,3,4])
# print(df)

# df = pd.DataFrame({'Name' : ['Prem', 'Jay','Purvik','Jainam'],
#                    'Age' : [20,19,21,22],
#                    'Gender' : ['Male','Male','Male','Female']},
#                   index=['A','B','C','D'])
# print(df)

df = pd.DataFrame({'Name' : ['Prem', 'Jay','Purvik','Jainam'],
                   'Age' : [20,19,21,22],
                   'Gender' : ['Male','Male','Male','Female']},
                  index=[1,2,3,4])
print(df.to_string(index=False))                         ## to_string ==> to convert result into string format
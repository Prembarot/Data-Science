import pandas as pd

data = {
    "Name": ["Prem", "Jay", "Jainam", "Purvik", "Jahnvl", "Ruchhl"],
    "Age": [25, None, 35, None, 45, None],
    "City": ["New York", "Paris", None, "Berlin", "Tokyo", None]
}

df = pd.DataFrame(data)
print(df)

# #  find rows with missing values
# print("\nRows with missing values:")
# print(df[df.isnull().any(axis=1)])
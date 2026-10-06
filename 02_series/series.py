import pandas as pd

# Series = A Pandas 1-Dimensional labeled array that can hold any data type
#          Think of it like a single column in a spreadsheet (1D)

data = [100, 102, 104, 200, 202]

series = pd.Series(data)
series2 = pd.Series(data, index=["a", "b", "c", "d", "f"])

print(series2)
print(series2.loc["a"]) # locate by the index

series2.loc["c"] = 106
print(series2)

print(series2.iloc[2]) # locate by an integer

# filter
print(series2[series2 >= 200])
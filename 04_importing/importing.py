import pandas as pd

df = pd.read_csv("pokemon.csv")

# print(df) #Truncated format (means only shows the first and last data set in the file)

# print(df.to_string())  # shows everything inside the file


df2 = pd.read_json("data.json")

print(df2.to_string())
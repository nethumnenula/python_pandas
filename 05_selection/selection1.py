import pandas as pd

# df = pd.read_csv("pokemon.csv") # This type for columns
df = pd.read_csv("pokemon.csv", index_col="Name")  # This type for rows

# SELECTION BY COLUMN
# print(df["Name"].to_string())
# print(df["Type 1"].to_string())
# print(df[["Name","Type 1","HP"]].to_string())

# SELECTION BY ROW/S
# print(df.loc["Pikachu"])
# print(df.loc["Charizard"])
# print(df.loc["Pikachu", ["Type 1", "HP"]])
# print(df.loc["Charizard":"Pikachu", ["Type 1", "HP"]])
print(df.iloc[0:11:2, 0:3]) # Integer selection
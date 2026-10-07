import pandas as pd
# Reduces a set of vales into a single summary value
# Used to summarize and analyze data
# Often used with the groupby() function

df = pd.read_csv("pokemon.csv", index_col="Name")

# Apply to WHOLE DATA SET
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())


# SINGLE COLUMNS ONLY
# print(df["HP"].mean())
# print(df["HP"].sum())
# print(df["HP"].min())
# print(df["HP"].max())
# print(df["HP"].count())



# groupby
group = df.groupby("Type 1")
print(group["Attack"].mean())
print(group["Attack"].sum())
print(group["Attack"].min())
print(group["Attack"].max())
print(group["Attack"].count())

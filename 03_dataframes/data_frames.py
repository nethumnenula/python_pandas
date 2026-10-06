import pandas as pd

# DataFrame = A tabular data structure with rows AND columns. (2D)
#             Similar to an Excel spreadsheet

data = {"Name": ["Nethum", "Nenula", "Me"],
        "Age": [30, 22, 20]}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])


print(df)
#print(df.loc["a"])
#print(df.iloc[1])

# Add a new column
df["Position"] = ["SE", "N/A", "NE"]

# Add a new Row

new_row = pd.DataFrame([{"Name": "He", "Age": 21, "Position": "FD"}],
                       index=["Employee 4"])
df = pd.concat([df, new_row])


# Add new rows
new_rows = pd.DataFrame([{"Name": "He", "Age": 21, "Position": "FD"},
                              {"Name": "He", "Age": 21, "Position": "FD"},
                              {"Name": "He", "Age": 21, "Position": "FD"}],
                       index=["Employee 5", "Employee 6", "Employee 7"])
df = pd.concat([df, new_rows])

print(df)
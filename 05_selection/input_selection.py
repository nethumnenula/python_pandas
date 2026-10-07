import pandas as pd

df = pd.read_csv("pokemon.csv", index_col="Name")


while True:
    try:
        name = input("Enter a Pokemon name: ").capitalize()
        print(df.loc[name])
        break
    except KeyError:
        print(f"Nothing found! Try again")





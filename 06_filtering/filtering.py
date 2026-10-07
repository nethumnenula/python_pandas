import pandas as pd


df = pd.read_csv("pokemon.csv", index_col="Name")

attack_pokemon = df[df["Attack"] >= 180]

legendary_pokemon = df[df["Legendary"] == True]

water_pokemon = df[(df["Type 1"] == "Water") | (df["Type 2"] == "Water")]

ff = df[(df["Type 1"] == "Fire") & (df["Type 2"] == "Flying")]

print(ff.to_string())
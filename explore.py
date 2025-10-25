import pandas as pd

df = pd.read_csv("lines.csv")
uniques = df[["conductor", "MOT"]]
uniques = uniques.drop_duplicates()
print(uniques.count)

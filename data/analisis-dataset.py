import pandas as pd
df = pd.read_csv("data/ai4i2020.csv")

print(df.head())
print(df.info())


df = df.drop_duplicates()


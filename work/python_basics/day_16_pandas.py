import pandas as pd

df = pd.read_csv("../data/pandas.csv")
print(df.head())
print("Количество строк и столбцов:", df.shape)
print("Столбцы:")
print(df.columns.tolist())
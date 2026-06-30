import pandas as pd

# Открыть CSV через pandas
df = pd.read_csv("../data/pandas.csv")


# Вывести первые 5 строк
print("Первые 5 строк:")
print(df.head())


# Посчитать строки и столбцы
print("Количество строк и столбцов:")
print(df.shape)


# Вывести список столбцов
print("Столбцы:")
print(df.columns.tolist())


# Найти пропуски
print("Пропуски:")
print(df.isnull().sum())


# Найти дубли
print("Количество дублей:")
print(df.duplicated().sum())
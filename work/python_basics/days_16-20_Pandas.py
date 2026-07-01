import pandas as pd

df = pd.read_csv("../data/.pandas.csv")

print("Первые 5 строк:")
print(df.head())

print("\nКоличество строк и столбцов:")
print(df.shape)

print("\nСтолбцы:")
print(df.columns.tolist())

print("\nПропуски:")
print(df.isnull().sum())

print("\nКоличество дублей:")
print(df.duplicated().sum())

print("\nЗаявки высокого приоритета:")
high_priority = df[df["приоритет"] == "Высокий"]
print(high_priority)

print("\nЗаявки из Перми:")
perm_requests = df[df["город"] == "Пермь"]
print(perm_requests)

print("\nКоличество заявок по приоритетам:")
priority_count = df["приоритет"].value_counts()
print(priority_count)
clean_df = df.drop_duplicates()

clean_df.to_csv("../data/.clean_pandas.csv", index=False)

print("\nОчищенная таблица сохранена!")
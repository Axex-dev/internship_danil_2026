import csv

count = 0
with open("../data/requests.csv", "r", encoding="utf-8") as f:# Прочитать CSV
    reader = csv.reader(f)
    for row in reader:
        print(row) # Вывести все строки
        count += 1 # Посчитать количество строк
        if len(row) < 5 or not row[4].strip(): # Найти строки без города
            print(f"Город в заявке {row[0]} не указан.")
        if len(row) < 5 or not row[3].strip(): # Найти строки без приоритета
            print(f"Приоритет в заявке {row[0]} не указан.")
with open("../data/requests.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f) # Преобразовать строку CSV в словарь
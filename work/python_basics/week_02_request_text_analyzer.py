import json

with open("../data/week_02_request_analysis_keywords.json", "r", encoding="utf-8") as file:
    keywords = json.load(file)


def write_request_to_file():
    with open("../data/week_02_request_analysis.txt", "w", encoding="utf-8") as file:
        n = int(input("Сколько заявок: "))
        for i in range(n):
            text = input(f"Заявка №{i + 1}: ")
            file.write(f"{i + 1}. {text}\n")


def normalize_text(text):
    return " ".join(text.strip().lower().split())


def find_keywords(text):
    found = []
    for keyword in keywords:
        if keyword.lower() in text:
            found.append(keyword)
    return found

write_request_to_file()
total_requests = 0
requests_with_keywords = 0
results = []

with open("../data/week_02_request_analysis.txt", "r", encoding="utf-8") as file:
    for line in file:
        total_requests += 1
        normalized_line = normalize_text(line)
        found_keywords = find_keywords(normalized_line)
        if found_keywords:
            requests_with_keywords += 1
        result = (
            f"Строка {total_requests}: "
            f"Найдено {len(found_keywords)} ключевых слов "
            f"({', '.join(found_keywords) if found_keywords else 'нет'})"
        )
        results.append(result)

with open("../results/week_02_request_analysis_result.txt", "w", encoding="utf-8") as file:
    for result in results:
        file.write(result + "\n")

    file.write(f"\nВсего строк: {total_requests}\n")
    file.write(f"Строк с ключевыми словами: {requests_with_keywords}\n")

print(f"Обработано строк: {total_requests}")
print(f"Строк с ключевыми словами: {requests_with_keywords}")
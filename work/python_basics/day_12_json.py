import json

zayavki = [
    {"id": 1, "name": "Иван Иванов", "status": "В обработке"},
    {"id": 2, "name": "Петр Петров", "status": "Одобрено"},
    {"id": 3, "name": "Анна Смирнова", "status": "Отклонено"},
]

with open("../data/request.json", "w", encoding="utf-8") as f:
    json.dump(zayavki, f, ensure_ascii=False, indent=2)

with open("../data/request.json","r", encoding="utf-8") as f:
    requests = f.read()
    for request in json.loads(requests):
        print(f"Номер: {request['id']} | Имя: {request['name']} | Статус: {request['status']}")
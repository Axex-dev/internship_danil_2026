# 1. Создать словарь student (Данные стажера сохранены)
student = {
    "full_name": "Данил Игоревич Теплоухов",
    "age": 15,
    "school": "Экономическая школа № 145",
    "grade": 8
}
# 2. Вывести ФИО из словаря	(ФИО отображается)
print(student.get("full_name"))
# 3. Вывести школу из словаря (Школа отображается)
print(student.get("school"))
# 4. Изменить класс на 9 (Значение обновлено)
student["school"] = 9
print(student.get("school"))
# 5. Добавить поле internship_start (Поле добавлено)
student["internship_start"] = '2026_06_08'
print('-'*99)
# 6. Создать словарь task (Задача описана)
task = {"name": "изучить переменные", "status": "none"}
# 7. Изменить статус задачи (Статус обновлен)
task['status'] = 'done'
print(f'Статус обновлен: {task}')
print('-'*99)
# 8. Создать словарь request (Учебная заявка описана)
request = {
    "id": 1,
    "text": "Заявка на курс Python",
    "status": "pending"
}
print(request)
print('-'*99)
# 9. Создать список из 3 заявок	(Список создан)
requests_task = [
    {"id": 1, "text": "Заявка на курс Python", "status": "pending"},
    {"id": 2, "text": "Заявка на курс Data Science", "status": "pending"},
    {"id": 3, "text": "Заявка на курс Machine Learning", "status": "pending"}
]
# 10. Вывести тексты всех заявок (Вывод работает)
for task in requests_task:
    print(task['text'])
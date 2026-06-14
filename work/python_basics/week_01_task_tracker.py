# week_01_task_tracker.py

tasks = [
    {"name": "изучить переменные", "priority": "high", "status": "done"},
    {"name": "изучить условия", "priority": "high", "status": "done"},
    {"name": "изучить списки", "priority": "medium", "status": "in_progress"},
    {"name": "изучить циклы", "priority": "medium", "status": "new"}
]

print("=== ТРЕКЕР УЧЕБНЫХ ЗАДАЧ ===\n")

print("Список задач:")

for task in tasks:
    print(
        f"- {task['name']} | "
        f"Приоритет: {task['priority']} | "
        f"Статус: {task['status']}"
    )

total_tasks = len(tasks)

high_priority_tasks = 0
completed_tasks = 0

for task in tasks:
    if task["priority"] == "high":
        high_priority_tasks += 1

    if task["status"] == "done":
        completed_tasks += 1

print("\n=== ИТОГ ===")
print(f"Всего задач: {total_tasks}")
print(f"Задач высокого приоритета: {high_priority_tasks}")
print(f"Выполненных задач: {completed_tasks}")
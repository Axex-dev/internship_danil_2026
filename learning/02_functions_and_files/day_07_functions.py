def sum_nums(num1, num2):
    return num1 + num2
print(sum_nums(int(input("введите 1 число ")), int(input("введите 2 число "))))
def hours_per_week(hours = 4):
    return hours * 5
print(hours_per_week(4))
def age(age =18):
    if age >= 18:
        print(f'ваш возраст подходит: {age}')
    else:
        print(f'ваш возраст не подходит: {age}')
def text(ttext):
    if len(ttext) == 0:
        print('ваш текст не имеет символов')
    elif ttext.isspace():
        print('ваш текст содержит только пробелы')
    else:
        print('ваш текст содержит символы')
text(input('введите текст '))
def fio(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
fio(first_name = 'Alex', last_name = 'Smith', middle_name = 'Bob')
tasks = [
    {"name": "изучить переменные", "priority": "high"},
    {"name": "изучить условия", "priority": "high"},
    {"name": "изучить списки", "priority": "medium"},
    {"name": "изучить циклы", "priority": "medium"}
]
def priority(**kwargs):
    print('Задачи с высоким приоритетом:')
    for task in tasks:
        if task['priority'] == "high":
            print(f' * {task["name"]}: {task["priority"]}')
        else:
            break
priority(tasks = tasks)
print('Все задачи: ')
def print_tasks(tasks,number):
    for task in tasks:
        print(f'{task["name"]}: {task["priority"]}')
        number += 1
print_tasks(tasks = tasks, number = 0)

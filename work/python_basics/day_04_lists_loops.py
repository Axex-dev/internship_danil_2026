topics = [
    "переменные",
    "условия",
    "списки",
    "циклы",
    "функции"
]
print(topics[0])  # Вывод: переменные
print(topics[-1])  # Вывод: функции
print(len(topics))  # Вывод: 5 (кол-во элементов списка)
print('Длинна списка: ', len(topics)) # Длина списка
topics.append("файлы")  # Добавление в список элемент 'файлы'

for topic in topics:  # проходит по всем элементам списка
    print(topic)
for number, topic in enumerate(topics):  # number принимает номер элемента, topic принимает значение элемента topics
    print(f"{number + 1}. {topic}")
# список numbers принимает числа
numbers = [int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))]
sum_numbers = sum(numbers) # сумма чисел
print("Сумма чисел:", sum_numbers)
for number in numbers:  # проходит по всем элементам списка
    if number > 10: # проверка больше/меньше
        print(f"Число больше 10: {number}")
print('Введите 5 задач: ')
# список tasks принимает числа
tasks = [
    input('Задача №1: '),
    input('Задача №2: '),
    input('Задача №3: '),
    input('Задача №4: '),
    input('Задача №5: ')
]
for task in tasks: # проходит по всем элементам списка
    if 'Python' in task or 'python' in task:
        print(f'Задачи Python: {task}')
# Возможные ошибки:
#topics = [
#    "переменные",
#    "условия",
#    "списки",
#    "циклы",
#    "функции"
#]
#print(topics[5])  # Вывод: ошибка (IndentationError: unindent does not match any outer indentation level)

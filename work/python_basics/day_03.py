age = int(input('Твой возраст: '))
hours_per_day = int(input('Часов в день: '))
# Проверка возраста
if age<16:
    print('Стажер младше 16 лет')
else:
    print('Стажер 16 лет или старше')
print('-' * 99)
# Проверка часов в день
if hours_per_day <= 4:
    print("Занятость не превышает 4 часа в день")
else:
    print("Нужно проверить режим занятости")
print('-' * 99)
# Проверка на класс (T or F)
print(int(input('Твой класс: '))==9)
print('-'*99)
# Проверка числа на положительность (T or F)
number = int(input('Любое положительное число: '))
print(number>0)
print('-'*99)
# Проверка числа на четность
if number%2==0:
    print('число четное')
else:
    print('число нечетное')
print('-'*99)
# Проверить пустую строку (Вывод Текст пустой)
string = input('Введите текст: ')
if string == '':
    print('Текст пустой', string=='')
else:
    print('Текст не пустой', string=='')
print('-'*99)
# Проверить приоритет задачи (Вывод по high/medium/low)
task = ['task1', 'task2', 'task3']
if task[0]:
    print('low')
elif task[1]:
    print('medium')
elif task[2]:
    print('high')

# Сделать ошибку в отступах
#if true:
#print('true')
#elif not true:
#print('false')
#else:
#print('no')

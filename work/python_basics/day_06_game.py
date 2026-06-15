import random
from time import time

knowledge = {
    "Математика": [
        {"question": "Сколько будет 2+2?", "answer": "4"},
        {"question": "Чему равен квадрат числа 3?", "answer": "9"}
    ],
    "История": [
        {"question": "В каком году началась Вторая мировая война?", "answer": "1939"},
        {"question": "Кто был первым президентом США?", "answer": "Джордж Вашингтон"}
    ],
    "Информатика": [
        {"question": "Сколько бит в одном гигабайте?", "answer": "8000000000"},
        {"question": "Сколько бит информации содержит файл объёмом 256 КБ?", "answer": "2097152"}
    ],
    "Физика": [
        {"question": "Как называется сила, которая всегда направлена против движения тела и возникает при соприкосновении поверхностей?", "answer": "Сила трения"},
        {"question": "Что произойдёт с ускорением тела, если при постоянной массе силу, действующую на него, увеличить в 2 раза?", "answer": "Увеличится в 2 раза"}
    ]
}
score = 0
miss = 0
start = time()
while score < 5:
    print("=== ВИТОРИНА ===")
    subject = random.choice(list(knowledge.keys()))
    question = random.choice(knowledge[subject])

    print("Тема:", subject)
    print("Вопрос:", question["question"])

    answer = input("Ответ: ")
    if answer == question["answer"]:
        print("Этот ответ верный!")
        score += 1
    else:
        print("Это неправильный ответ!")
        miss += 1
    print(f'Очки: {score}')
end = time()
print(f"Вы выйграли!\n Ваша статистика:\nОчки: {score}\nНеправильные ответы: {miss}\nВремя на ответы: {int(end - start)} секунд")
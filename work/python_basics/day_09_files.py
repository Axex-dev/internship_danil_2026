import json

with open("../data/students.json", "r", encoding="utf-8") as file:
    data = json.load(file)

def middle_grade(grades):
    return sum(grades) / len(grades)


with open("../data/grades_analysis.txt", "w", encoding="utf-8") as file:
    file.write("Name:\t Grades:\t\t Avg. grade\n")
    for student in data:
        avg = middle_grade(student["grades"])
        file.write(f"{student['name']} | {student['grades']} | {avg:.2f}\n")
# чтоб закинуть в пул
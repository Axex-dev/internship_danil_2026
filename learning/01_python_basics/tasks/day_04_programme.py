ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print (ages)
print ('Min. age: ', min(ages))
print ('Max. age: ', max(ages))
len_ages = len(ages)
if len_ages % 2 == 0:
    median = (ages[len_ages//2 - 1] + ages[len_ages//2]) / 2
else:
    median = ages[len_ages//2]

print(f'Медианный возраст: {median}')
print(f'Средний возраст: {sum(ages)/len(ages)}')
print(f'Разница в возрасте: {max(ages)-min(ages)}')
A = abs(min(ages) - sum(ages)/len_ages)
B = abs(max(ages) - sum(ages)/len_ages)
if A < B:
    print("|min - avg| < |max - avg|")
elif A > B:
    print("|min - avg| > |max - avg|")
else:
    print("|min - avg| = |max - avg|")
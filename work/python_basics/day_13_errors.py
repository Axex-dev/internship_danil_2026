try:
    f = open('../data/request.json', "r", encoding="utf-8")
except FileNotFoundError:
    print('-')
else:
    print(f)
finally:
    print('Finish')
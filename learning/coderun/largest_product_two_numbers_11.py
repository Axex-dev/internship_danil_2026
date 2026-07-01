numbers = [int(i) for i in input().split()]
numbers.sort(reverse=True)
if numbers[0] * numbers[1] > numbers[-1] * numbers[-2]:
    max_number = [numbers[0], numbers[1]]
    print(min(max_number), max(max_number))
else:
    min_number = [numbers[-1], numbers[-2]]
    print(min(min_number), max(min_number))

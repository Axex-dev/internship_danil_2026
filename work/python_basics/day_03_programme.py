import math
while True:
    print('Rectangle operation:\n  1. rectangle area\n  2. rectangle perimetr')
    print('Circle operation:\n  3. circle area\n  4. circle length')
    print('Triangle operation:\n  5. triangle area')
    print('Cube operation:\n  6. cube surface area\n  7. cube volume')
    answer: int = int(input('Pick a number: '))
    if answer == 1:
        print('Rectangle area: ',(int(input('Enter lengths: ')) * int(input('Enter widths: '))))
    elif answer == 2:
        print('Rectangle perimetr: ',(int(input('Enter lengths: ')) + int(input('Enter widths: ')))*2)
    elif answer == 3:
        print('Circle area: ', float(input('Enter radius: '))**2 * 3.14)
    elif answer == 4:
        print('Circle length: ', int(input('Enter diameter: '))*3.14)
    elif answer == 5:
        a_side = int(input('Enter a-side: '))
        b_side = int(input('Enter b-side: '))
        c_side = int(input('Enter c-side: '))
        half_meter = (a_side + b_side + c_side) / 2
        area = math.sqrt(half_meter * (half_meter- a_side) * (half_meter - b_side) * (half_meter - c_side))
        print('Triangle area: ', area)
    elif answer == 6:
        print('Cube surface area: ', 6 * int(input('Enter a cube edge length: '))**2)
    elif answer == 7:
        print('Cube volume: ', int(input('Enter a cube edge length: '))**3)
    else:
        print('Invalid input')
        break
    input('Press enter to continue')
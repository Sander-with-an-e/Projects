from math import sqrt
print('Solve ax^2 + bx + c = 0')
a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

if not a == 0:
    D = b ** 2.0 - 4.0 * a * c
    if D > 0:
            x1 = (-b - sqrt(D)) / (2.0 * a)
            x2 = (-b + sqrt(D)) / (2.0 * a)
            print('There are two solutions:', round(x1, 3), 'and', round(x2,
            3))
    elif D < 0:
        print('There are no solutions')
    else:
        x = -b / (2.0 * a)
        print('There is one solution:', round(x, 3))
else:
        x = -c / b
        print('There is one solution:', round(x, 3))
print('\nReady.')



from math import sin, radians, sqrt, cos

a = int(input('Введите значение для переменной: a = '))
b = int(input('Введите значение для переменной: b = '))
x = int(input('Введите значение для переменной: x = '))
y = int(input('Введите значение для переменной: y = '))
n = int(input('Введите значение для переменной: n = '))

print(f'a) 2 * x = {2 * x}')
print(f'б) sin(x) = {round(sin(radians(x)), 2)}')
print(f'в) a^2 = {a ** 2}')
print(f'г) sqrt(x) = {round(sqrt(x), 2)}, {round(x ** 0.5, 2)}')
print(f'д) abs(n) = {abs(n)}')
print(f'е) 5 * cos(y) = {5 * round(cos(radians(y)), 2)}')
print(f'ж) -7,5 * a ** 2 = {-7,5 * a * a}')
print(f'з) 3 * sqrt(x) = {round(3 * sqrt(x), 2)}, {round(3 * x ** 0.5, 2)}')
print(f'и) sin(a) * cos(b) + cos(a) * sin(b) = {round(sin(radians(a)), 2) * round(cos(radians(b)), 2) + round(cos(radians(a)), 2) * round(sin(radians(b)), 2)}')
print(f'к) a sqrt(2 * b) = {round(a * sqrt(2 * b), 2)}, {round(a * 2 * b ** 0.5, 2)}')
print(f'л) 3 * sin(2 * a) * cos(3 * b) = {3 * round(sin(radians(2 * a)), 2) * round(cos(radians(3 * b)), 2)}')
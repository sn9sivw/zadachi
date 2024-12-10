from math import sqrt
a = float(input("Длина большего основания:"))
b = float(input("Длина меньшего основания:"))
h = float(input("Высота:"))
print("P =", a + b + 2 * sqrt(sqrt(h) + sqrt(a - b) / 4))

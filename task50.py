x1 = int(input("Введите координату x1: "))
y1 = int(input("Введите координату y1: "))
x2 = int(input("Введите координату x2: "))
y2 = int(input("Введите координату y2: "))
x3 = int(input("Введите координату x3: "))
y3 = int(input("Введите координату y3: "))
lx1 = abs(x1 - x2)
ly1 = abs(y1 - y2)
lx2 = abs(x2 - x3)
ly2 = abs(y2 - y3)
lx3 = abs(x3 - x1)
ly3 = abs(y3 - y1)
side1 = s = round(((lx1 ** 2) + (ly1 ** 2)) ** 0.5, 2)
side2 = s = round(((lx2 ** 2) + (ly2 ** 2)) ** 0.5, 2)
side3 = s = round(((lx3 ** 2) + (ly3 ** 2)) ** 0.5, 2)
p = side1 + side2 + side3
s = round(((p / 2) * (
        (p / 2) - side1) * ((p / 2) - side2) * ((p / 2) - side3)) ** 0.5, 2)
print("Периметр = ", p)
print("Площадь = ", s)

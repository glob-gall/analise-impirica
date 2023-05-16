from math import*

a = float(input("a: "))
b = float(input("b: "))
y = radians(float(input("angulo: ")))

j = a**2 + b**2 - 2*a*b * cos(y)

c = sqrt(j)


print(round(c, 2))
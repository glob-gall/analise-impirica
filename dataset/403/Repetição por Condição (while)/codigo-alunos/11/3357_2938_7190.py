from math import*

a = float(input("a:"))
b = float(input("b:"))
g = radians(float(input("angulo:")))

c = sqrt(a**2 + b**2 - 2*a*b*cos(g))

print(round(c, 2))
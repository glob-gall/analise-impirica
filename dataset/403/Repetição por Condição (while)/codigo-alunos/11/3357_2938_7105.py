from math import *
a = float(input())
b = float(input())
angulo = radians(float(input()))

c= sqrt(a**2 + b**2 - 2*a*b*cos(angulo))

print(round(c, 2))
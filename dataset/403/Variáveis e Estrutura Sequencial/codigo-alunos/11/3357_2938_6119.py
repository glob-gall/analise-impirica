from math import*

a = float(input("Distancia a: "))
b = float(input("Distancia b: "))
y = radians(float(input("Angulo entre a e b: ")))

c = sqrt(a**2+b**2-(2*(a*b)*cos(y)))

print(round(c,2))
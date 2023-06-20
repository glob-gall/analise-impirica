from math import *
a = float(input("Distancia para arvore 1: "))
b = float(input("Distancia para arvore 2: "))
ang  = radians(float(input("Angulo entre A e B: ")))
C = sqrt(a**2 + b**2 - 2*a*b*cos(ang))
print(round(C,2))					
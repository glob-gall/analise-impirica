from math import *

a = float(input("Informe a distancia entre a distancia a:"))
b = float(input("Informe a distancia entre a distancia a:"))
gamma = float(input("Informe o valor de gama:"))

c = sqrt((a**2) + (b**2) - 2*a*b*cos(radians(gamma)))

print(round(c, 2))
from math import *

a = float(input("distancia um"))
b = float(input("distancia dois"))
g = float(input("gamma"))
c = sqrt((a**2)+(b**2)-2*a*b*cos(radians(g)))
print(round(c,2))
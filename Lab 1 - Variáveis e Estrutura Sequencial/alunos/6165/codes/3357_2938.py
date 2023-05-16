from math import *

a = float(input("Digite a distancia A entre o observador e a primeira arvore: "))
b = float(input("Digite a distancia de B entre o obersvador e a segunda arvore: "))
ang = float(input("Digite o angulo y entre A e B: "))

x = (a**2)+(b**2)-2*a*b*cos(radians(ang))
c = sqrt(x)

print(round(c, 2))
from math import *

a = float(input("Digite a distancia entre o observador e a primeira arvore: "))
b = float(input("Digite a distancia entre o observador e a segunda arvore: "))
ang = radians(float(input("Digite o angulo entre a e b: ")))

c = sqrt(a ** 2 + b ** 2 - 2 * a * b * cos(ang))
print(round(c,2))
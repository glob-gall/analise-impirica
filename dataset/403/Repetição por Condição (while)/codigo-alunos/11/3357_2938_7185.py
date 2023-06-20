from math import *
a = float(input("Digite a distancia a entre o observador e A primeira arvore: "))
b = float(input("Digite a distancia a entre o observador e B segunda arvore: "))
ang_y = radians (float(input("Digite o angulo y entre a e b: ")))
c = sqrt((a**2) + (b**2) - (2 * a * b) * (cos(ang_y)))
print (round(c, 2))
from math import *
a = float(input("digite a distancia 'a': "))
b = float(input("digite a distancia b entre o observador e a segunda arvore: "))
ang = radians(float(input("angulo entre 'a' e 'b': ")))

c = sqrt(a**(2) + b**(2) - 2*a*b*cos(ang))
print(round(c,2))
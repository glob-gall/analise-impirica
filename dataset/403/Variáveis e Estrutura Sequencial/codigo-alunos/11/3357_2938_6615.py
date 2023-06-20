from math import *  

a = float(input("digite a distancia entre o observador e a primeira arvore: "))
b = float(input("digite a distancia entre o observador e a segunda arvore: "))
A = radians(float(input("digite o angulo entre a e b: ")))

c = sqrt(a**2 + b**2 - 2 * a * b * cos(A))

print(round(c,2))
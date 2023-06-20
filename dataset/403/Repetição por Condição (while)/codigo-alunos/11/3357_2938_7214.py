from math import*
a = float(input("Digite a distancia do observador ate a primeira arvore: "))
b = float(input("Digite a distancia do observador ate a segunda arvore: "))
angulo = radians(float(input("Digite a distancia entre a e b: ")))

c = sqrt(a**2 + b**2 - 2*a*b*cos(angulo))

print(round(c,2))
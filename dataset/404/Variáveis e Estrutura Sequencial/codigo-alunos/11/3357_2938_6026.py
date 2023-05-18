from math import*


a= float(input("Digite a distancia: "))
b= float(input("Digite a distancia: "))
y= float(input("Digite um angulo: "))
x= radians(y)
c= sqrt(a**2+b**2-2*a*b*cos(x))

print(round(c, 2))
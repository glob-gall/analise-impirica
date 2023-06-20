# distancias
from math import*

a= float(input( "Digite a distancia entre a primeira arvore:"))
b= float(input( "Digite a distancia entre a segunda arvore:"))
angle= radians(float(input("Digite o angulo formado entre a distancia a e b:")))
			
c= sqrt(a**2 + b**2 -2*a*b * cos(angle))
print( round(c, 2))		  
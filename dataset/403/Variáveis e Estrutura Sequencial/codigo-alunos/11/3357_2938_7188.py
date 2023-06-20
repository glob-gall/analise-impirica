from math import*
a= float(input("distancia a"))
b= float(input("distancia b"))
d= radians(float(input("angulo a e b")))

c= sqrt((a**2)+ (b**2)- 2*(a*b)*cos(d))
print(round(c,2))
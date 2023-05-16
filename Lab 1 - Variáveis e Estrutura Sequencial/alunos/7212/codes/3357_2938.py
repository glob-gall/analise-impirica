from math import*
a= float(input())
b= float(input())
ang= radians(float(input()))

c= sqrt((a**2+b**2)-2*a*b*cos(ang))

print(round(c, 2))
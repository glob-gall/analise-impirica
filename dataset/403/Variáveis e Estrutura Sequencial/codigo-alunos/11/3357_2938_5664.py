from math import*
a= float(input('digite o lado a: '))
b= float(input('digite o lado b: '))
y= radians(float(input('digite o angulo y: ')))


c = sqrt(a**2+b**2-2*a*b*cos(y))

print(round(c,2))
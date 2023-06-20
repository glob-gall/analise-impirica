from math import *
da = float(input("diatancia entre observador e arvore: "))
db = float(input("diatancia entre observador e segunda arvore: "))
dc = radians(float(input("angulo entre a e b:  ")))
c = sqrt((da**2)+(db**2)-(2*da*db)*cos(dc))
print(round(c, 2))


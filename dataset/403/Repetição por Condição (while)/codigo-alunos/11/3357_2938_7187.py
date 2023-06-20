from math import *

da= float(input("distancia entre o observador e a primeira arvore "))
db = float(input("distancia entre o observador e a segunda arvore "))
angulo = radians(float(input("angulo entre a e b")))

c = sqrt(da ** 2 + db ** 2 - 2 * da * db * cos(angulo))

print(round(c, 2))

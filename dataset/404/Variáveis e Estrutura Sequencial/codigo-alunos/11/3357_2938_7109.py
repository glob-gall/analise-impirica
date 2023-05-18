from math import*
"""

"""

a = float(input("Digite a distancia 'a': "))
b = float(input("Digite a distancia 'b': "))
v = float(input("Digite o valor do angulo entre eles: "))
z = radians(v)
c = sqrt((a**2) + (b**2) - (2 * a * b)*(cos(z)))
print(round(c, 2))
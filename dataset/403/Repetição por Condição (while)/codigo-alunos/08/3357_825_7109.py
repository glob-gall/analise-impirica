from math import*
"""
Escreva um programa que leia o valor de um raio r, inserido via teclado.

Como saída, determine as seguintes informações, nesta ordem:

Área de um círculo com o raio r.
Volume de uma esfera com raio r.
Arredonde os resultados com até 03 casas decimais de precisão.

"""
r = float(input("Digite o valor do raio: "))
a = pi*(r**2)
v = 4/3*pi*(r**3)
print(round(a, 3))
print(round(v, 3))

from math import*
"""
Escreva um programa que leia os comprimentos dos lados de um triângulo.
Como saída, determine a sua área arredondada com até cinco casas decimais.

"""
a = float(input("Digite um valor para o lado 'a': "))
b = float(input("Digite um valor para o lado 'b': "))
c = float(input("Digite um valor para o lado 'c': "))
s = (a + b + c)/2
area = sqrt(s*(s - a)*(s - b)*(s - c))
print(round(area, 5))
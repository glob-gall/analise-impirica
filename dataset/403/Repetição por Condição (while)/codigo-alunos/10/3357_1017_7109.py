from math import*
"""
Escreva um programa que leia as seguintes informações, medidas em graus:

A latitude t1 de um ponto P1.
A longitude g1 de um ponto P1.
A latitude t2 de um ponto P2.
A longitude g2 de um ponto P2.
"""

t1 = radians(float(input("Latitude de t1 em um ponto P1: ")))
g1 = radians(float(input("Latitude de g1 em um ponto P1: ")))
t2 = radians(float(input("Latitude de t2 em um ponto P2: ")))
g2 = radians(float(input("Latitude de g2 em um ponto P2: ")))
r = 6371.01
d = r * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2))
print(round(d,  2))
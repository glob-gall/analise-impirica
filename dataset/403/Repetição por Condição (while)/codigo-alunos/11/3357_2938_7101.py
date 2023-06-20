#distância a entre o observador e a primeira árvore.
irineu = float(input("distancia a entre o observador e a primeira arvore:"))
#distância b entre o observador e a segunda árvore.
batman = float(input("distancia b entre o observador e a segunda arvore:"))
#angulo γ entre a e b (em graus).
from math import*
jorge = radians(float(input("angulo y entre a e b:")))
c = (irineu**2 + batman**2 - 2 * irineu * batman * cos(jorge))**0.5
print(round(c, 2))
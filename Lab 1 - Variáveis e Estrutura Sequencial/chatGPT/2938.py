import math

a = float(input("Digite a distância entre o observador e a primeira árvore: "))
b = float(input("Digite a distância entre o observador e a segunda árvore: "))
gamma = math.radians(float(input("Digite o ângulo entre a e b em graus: ")))

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(gamma))
c_arredondado = round(c, 2)

print(c_arredondado)

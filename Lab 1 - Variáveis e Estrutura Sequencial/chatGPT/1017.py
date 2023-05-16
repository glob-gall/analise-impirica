import math

t1 = math.radians(float(input("Digite a latitude de P1 em graus: ")))
g1 = math.radians(float(input("Digite a longitude de P1 em graus: ")))
t2 = math.radians(float(input("Digite a latitude de P2 em graus: ")))
g2 = math.radians(float(input("Digite a longitude de P2 em graus: ")))

R = 6371.01  # Raio médio da Terra em quilômetros

d = R * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

d_arredondada = round(d, 2)

print(d_arredondada)

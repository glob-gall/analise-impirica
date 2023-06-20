from math import*

# Leitura de entradas
dista = float (input("Digite a distancia entre o observador e a primeira arvore:"))
distb = float (input("Digite a distancia entre o observador e a segunda arvore:"))
angulo = radians (float (input("Digite o angulo entra dista e distb:")))
varc = sqrt(dista ** 2  + distb ** 2 - 2 * ( dista * distb * cos(angulo)))

# Impressao de saidas
print(round(varc, 2))

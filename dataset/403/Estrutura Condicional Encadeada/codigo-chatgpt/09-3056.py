area = float(input("Digite a área a ser fertilizada (em hectares): "))

if area < 0:
    print("Entrada inválida")
else:
    if area <= 10000:
        custo = 6.0
        fertilizante = 100.0
    elif area <= 20000:
        custo = 5.5
        fertilizante = 150.0
    elif area <= 30000:
        custo = 5.0
        fertilizante = 200.0
    else:
        custo = 4.5
        fertilizante = 250.0

    valor = area * custo + fertilizante
    print(round(valor, 2))
area = float(input("Digite a área a ser fertilizada (em hectares): "))

if area < 0:
    print("Entrada inválida")
else:
    if area <= 10000:
        custo = 6.0
        fertilizante = 100.0
    elif area <= 20000:
        custo = 5.5
        fertilizante = 150.0
    elif area <= 30000:
        custo = 5.0
        fertilizante = 200.0
    else:
        custo = 4.5
        fertilizante = 250.0

    valor = area * custo + fertilizante
    print(round(valor, 2))

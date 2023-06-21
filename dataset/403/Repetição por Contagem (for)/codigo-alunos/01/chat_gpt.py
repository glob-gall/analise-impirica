def contar_multas(velocidades):
    limite_velocidade = velocidades[0]
    multas = 0

    for velocidade in velocidades[1:]:
        limite_superado = velocidade > limite_velocidade
        percentual = (velocidade - limite_velocidade) / limite_velocidade * 100

        if limite_superado and 20 < percentual < 50:
            multas += 1

    return multas

# Exemplo de utilização:
velocidades = [60, 70, 80, 90, 100, 110, 120]
multas_graves = contar_multas(velocidades)
print("Número de multas graves:", multas_graves)

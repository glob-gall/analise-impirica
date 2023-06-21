nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

peso1 = 1
peso2 = 2
peso3 = 3
peso4 = 4

# Calcular a média ponderada
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3 + nota4 * peso4) / (peso1 + peso2 + peso3 + peso4)

# Arredondar a média para duas casas decimais
media_arredondada = round(media_ponderada, 2)

# Saída
print(media_arredondada)

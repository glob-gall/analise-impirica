ingredientes = {
    "ARROZ": 500,
    "CENOURA": 100,
    "KAMPYO": 20,
    "NORI": 50,
    "OMELETE": 200,
    "PEPINO": 150,
    "SALMAO": 300,
    "SHITAKE": 150
}

nome_ingrediente = input("Digite o nome do ingrediente: ").upper()
quantidade_receitas = int(input("Digite a quantidade de receitas que deseja preparar: "))

if nome_ingrediente in ingredientes and 1 <= quantidade_receitas <= 50:
    quantidade_ingrediente = ingredientes[nome_ingrediente] * quantidade_receitas
    print(quantidade_ingrediente)
else:
    print("Entrada invalida")

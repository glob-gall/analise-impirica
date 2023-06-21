def calcular_total_conta(produtos, quantidades):
    tabela_precos = {
        "ARROZ": 1.25,
        "FEIJAO": 2.60,
        "BIS": 1.80,
        "MIOJO": 0.85,
        "FANTA": 3.20
    }

    total = 0.0

    for produto, quantidade in zip(produtos, quantidades):
        preco = tabela_precos.get(produto, 0.0)
        total += preco * quantidade

    return total

# Exemplo de utilização:
produtos = ["FANTA", "FEIJAO", "ARROZ", "MIOJO"]
quantidades = [2, 3, 1, 4]

total_conta = calcular_total_conta(produtos, quantidades)
print(f"Total da conta: R$ {total_conta:.2f}")

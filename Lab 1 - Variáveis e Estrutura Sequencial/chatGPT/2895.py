quantidade_jogos = int(input("Digite a quantidade de jogos a serem encomendados: "))
valor_unitario = float(input("Digite o valor unitário de cada jogo: "))
valor_frete = float(input("Digite o valor do frete: "))

preco_total = (valor_unitario * quantidade_jogos) + valor_frete

print("O preço total a ser pago é:", preco_total)

# Leitura das entradas e conversao para float
quant = int(input("Quantos jogos voce deseja encomendar?"))
var = float(input("Qual o valor unitario do jogo?"))
frete = float(input("Qual o valor do frete?"))

# Calculo do valor a ser pago, incluindo o frete
total = var  * quant + frete

#  Impressao do valor total
print(total)
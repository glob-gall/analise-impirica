valor_vendas = float(input("Digite o valor de vendas do funcionário: "))

if valor_vendas <= 1000.00:
    comissao = valor_vendas * 0.05
else:
    comissao = 1000.00 * 0.05 + (valor_vendas - 1000.00) * 0.10

comissao = round(comissao, 2)
print("Valor da comissão a ser paga: R$", comissao)

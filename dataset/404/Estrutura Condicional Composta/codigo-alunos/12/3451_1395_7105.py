vendas = float(input())
if(vendas<=1000):
	comissao = vendas*0.05
if(vendas>1000):
	comissao = 1000*0.05 + (vendas-1000)*0.1
print(round(comissao,2))
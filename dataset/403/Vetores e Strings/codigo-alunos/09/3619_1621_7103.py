from numpy import*
produtos = array(eval(input()))
quant = array(eval(input()))

ar = 1.25
fe = 2.60
bis = 1.80
mi = 0.85
fa = 3.20

i = 0
conta = 0 

while i<size(produtos):
	if produtos[i].upper()=="ARROZ":
		conta = conta + ar*quant[i]
	elif produtos[i].upper()=="FEIJAO":
		conta = conta + fe*quant[i]
	elif produtos[i].upper()=="BIS":
		conta = conta + bis*quant[i]
	elif produtos[i].upper()=="MIOJO":
		conta = conta + mi*quant[i]
	elif produtos[i].upper()=="FANTA":
		conta = conta + fa*quant[i]
	i = i + 1
print(round(conta,2))

v = float(input("vendas: "))

if v <= 1000:
	comissao = v*0.05
	
else:
	comissao = (1000*0.05) + ((v-1000)*0.1)
	
print(round(comissao,2))
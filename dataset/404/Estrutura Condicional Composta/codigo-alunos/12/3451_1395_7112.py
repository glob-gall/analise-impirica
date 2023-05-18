i = float(input("Vendas: "))

M = float(1000)
if( i <= M):
	c = i * (5/100)
if( i > M):
	a = i - M
	c = (M * (5/100)) + (a *(10/100))
	
print(round(c,2))
hectares = float(input())

if(hectares<=10000):
	custo = hectares*5
if(hectares>10000):
	custo = 10000*5 +(hectares-10000)*4
print(round(custo,2))
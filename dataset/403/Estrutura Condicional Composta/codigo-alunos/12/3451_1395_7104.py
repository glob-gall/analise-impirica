valor = float(input())

if(valor<=1000):
	calculo = valor*0.05
	print(round(calculo,2))
else: 
	calculo = valor - 1000
	cal = (1000*0.05)+(calculo*0.10)
	
	
	print(round(cal,2))
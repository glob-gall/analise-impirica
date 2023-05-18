escala= input('escala: ').upper()
temp= float(input('temperatura: '))

if escala=="F":
	valor= (5/9)*(temp-32)
if escala=="C":
	valor = ((9/5)*temp)+32
	
print(round(valor,2))
	


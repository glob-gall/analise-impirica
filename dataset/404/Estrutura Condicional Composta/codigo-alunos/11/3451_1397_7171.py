#fertilização aérea

area= float(input("Digite a area a ser fertilizada (em Hectares):"))

if (area<= 10000):
   total= (area * 5)

else:
	total =((area - 10000) * 4) + (10000 * 5)
	
print(total)
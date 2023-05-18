nome= input('nome: ').upper()
q= int(input('quantidade: '))

if 0<q<50 and nome=='ARROZ':
	quant=q*500
	print(quant)
	
elif 0<q<50 and nome=='CENOURA':
	quant=q*100
	print(quant)
	
elif 0<q<50 and nome=='KAMPYO':
	quant=q*20
	print(quant)
	
elif 0<q<50 and nome=='NORI':
	quant=q*50
	print(quant)
	
elif 0<q<50 and nome=='OMELETE':
	quant=q*200
	print(quant)
	
elif 0<q<50 and nome=='PEPINO':
	quant=q*150
	print(quant)
	
elif 0<q<50 and nome=='SALMAO':
	quant=q*300
	print(quant)
	
elif 0<q<50 and nome=='SHITAKE':
	quant=q*150
	print(quant)
	
else:
	print('Entrada invalida')
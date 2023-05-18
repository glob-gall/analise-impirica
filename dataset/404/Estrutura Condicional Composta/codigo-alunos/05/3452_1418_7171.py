#eleições

cad1= int(input("Digite o numero de votos do candidado mais votado:"))
cad2= int(input("Digite o numero de votos do segundo candidado:"))
cad3= int(input("Digite o numero de votos do terceiro colocado:"))

votes= (cad1 + cad2 + cad3)
			 
if (votes>= 200000) and (cad1<= (votes/2)):
	print( "sim".upper())
	
else:
	 print( "nao".upper())
			 
ni = (input()).upper()
q = int(input())

if (q > 0 and q <= 50):
	
	if (ni == "ARROZ"):
		
		g = q * 500
		print (g)
		
	elif (ni == "CENOURA"):
		
		g = q * 100
		print (g)
		
	elif (ni == "KAMPYO"):
		
		g = q * 20
		print (g)
		
	elif (ni == "NORI"):
		
		g = q * 50
		print (g)
		
	elif (ni == "OMELETE"):
		
		g = q * 200
		print (g)
		
	elif (ni == "PEPINO"):
		
		g = q * 150
		print (g)
		
	elif (ni == "SALMAO"):
		
		g = q * 300
		print (g)
		
	elif (ni == "SHITAKE"):
		
		g = q * 150
		print (g)
		
	else:
		
		print ("Entrada invalida")
		
	
else:
	
	print ("Entrada invalida")

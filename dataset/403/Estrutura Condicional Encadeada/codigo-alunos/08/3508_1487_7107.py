n = input().upper()
q = int(input())

if( q > 0 and q < 50):
	
	if( n == 'ARROZ' ):
		qn = (q * 500)
		
	elif( n == 'CENOURA'):
		qn = (q * 100)
		
	elif( n == 'KAMPYO'):
		qn = (q * 20)
		
	elif( n == 'NORI'):
		qn = (q * 50)
		
	elif( n == 'OMELETE'):
		qn = (q * 200)
		
	elif( n == 'PEPINO' or n == 'SHITAKE'):
		qn = (q * 150)
		
	elif( n == 'SALMAO'):
		qn = (q * 300)
		
	else:
		print("Entrada invalida")
		
	print(qn)
	
else:
	print("Entrada invalida")
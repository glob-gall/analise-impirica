x = int(input("Numero de termos: "))

h=0
for i in range(1,x+1):
	sinal = (-1)**(i-1)
	h = sinal*(1/i)+h
print("H =",round(h,6))
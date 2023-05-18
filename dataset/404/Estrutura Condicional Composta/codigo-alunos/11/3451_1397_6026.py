a= float(input("Digite a area: "))

if(a<=10000):
	c=5*a
	print(round(c,2))
else: 
	ct= 5*10000
	v= a-10000
	b= v*4
	n= ct+b
	print(round(n,2))
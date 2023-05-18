a=float(input("area:"))
if(a>=0 and a<10000):
	c=6
	f=100
elif(a>=10000 and a<20000):
	c=5.50
	f=150
elif(a>=20000 and a<30000):
	c=5
	f=200
else:
	c=4.50
	f=250
x=(a*c)+f
print(round(x,2))
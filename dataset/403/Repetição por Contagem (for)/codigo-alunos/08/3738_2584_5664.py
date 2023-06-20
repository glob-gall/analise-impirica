n= int(input('n: '))

H=0
for i in range(n):
	H = H + ((-1)**i)/(i+1)
	
print('H =',round(H,6))
	
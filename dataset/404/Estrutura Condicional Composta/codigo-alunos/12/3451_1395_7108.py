v= float(input())

if(v<=1000):
	r=(v*0.05)
	print(round(r,2))
	
else:
	s= v-1000
	r= (1000*0.05)+(0.1*s)
	
	print(round(r,2))
	

	
vvendas=float(input())

if  	vvendas<=1000:
		comi = vvendas*0.05
		print(round(comi,2))
		
else:
		extra = vvendas - 1000
		comi = (vvendas * 0.05) + (extra * 0.05)		
		print(round(comi,2))
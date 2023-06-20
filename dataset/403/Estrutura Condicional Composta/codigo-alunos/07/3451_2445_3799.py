l=input("C ou F:")
x=float(input("num:"))
if(l=="C"):
	y=(9/5)*x+32
else:
	y=(5/9)*(x-32)
print(round(y,2))
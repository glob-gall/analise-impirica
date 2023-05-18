g= input()
t= float(input())
c= 5/9*(t-32)
f= (t*9/5)+32
if(g.upper()=="C"):
	print(round(f,2))
else:
	print(round(c,2))

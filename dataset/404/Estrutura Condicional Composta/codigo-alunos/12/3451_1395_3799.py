v=float(input("vendas:"))
if(v>1000):
	x=(1000*0.05)+(v-1000)*0.10
else:
	x=v*0.05
print(round(x,2))
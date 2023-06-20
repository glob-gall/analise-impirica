v = float(input())

if(v <= 1000):
	c = (v * 0.05) 
else:
	c = (1000 * 0.05) + ((v - 1000) * 0.1)

print(round(c,2))
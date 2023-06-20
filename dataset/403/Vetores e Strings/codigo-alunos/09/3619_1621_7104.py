from numpy import*

a = array(eval(input().upper()))
b = array(eval(input()))

i = 0
c = 0

while(i < size(a)):
	if a[i] == "ARROZ":
		c = c + 1.25 * b[i]
	if a[i] == "FEIJAO":
		c = c + 2.60 * b[i]
	if a[i] == "BIS":
		c = c + 1.80 * b[i]
	if a[i] == "MIOJO":
		c = c + 0.85 * b[i]
	if a[i] == "FANTA":
		c = c + 3.20 * b[i]
		
	i = i+1
	
print(round(c,2))

c1 = int(input())
c2 = int(input())
c3 = int(input())
if (c1 + c2 + c3 <= 200000):
	print ("NAO")
else:
	if (c1 <= (c1 + c2 + c3)/2):
		print ("SIM")
	else:
		print ("NAO")
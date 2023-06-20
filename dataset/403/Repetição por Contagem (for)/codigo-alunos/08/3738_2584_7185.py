# input

n = int(input())

# loop

for i in range(n + 1):
	
	if (i == 0):
		
		s = 0
		
	elif (i % 2 != 0):
		
		s = s + (1 / i)
		
	else:
		
		s = s - (1 / i)
		
	

# final

print ('H =', round(s, 6))
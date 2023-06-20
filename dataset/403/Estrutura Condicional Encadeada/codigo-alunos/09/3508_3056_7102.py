area = float(input())

if(0 <= area <= 10000):
	v = (area * 6) + 100
elif(10000 < area <= 20000):
	v = (area * 5.5) + 150
elif(20000 < area <= 30000):
	v = (area * 5) + 200
elif(30000 < area):
	v = (area * 4.5) + 250

print(round(v,2))
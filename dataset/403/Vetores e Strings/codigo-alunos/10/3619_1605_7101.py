from numpy import*
v = array(eval(input("n: ")))
i = 0
j = 200
while (i<size(v)):
	if (v[i]==1):
		j = j * 4
	elif (v[i]==2):
		j = j * 2
	elif (v[i]==4):
		j = j / 2
	i = i + 1
print(round(j,2))
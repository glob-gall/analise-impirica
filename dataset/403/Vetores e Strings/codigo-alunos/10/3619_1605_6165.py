from numpy import*

v = array(eval(input("Digite quais aneis foram acertados: ")))

i = 0
u = 200

while(i < size(v)):
		if(v[i] == 1):
			u = u * 4
		elif(v[i] == 2):
			u = u * 2
		elif(v[i] == 3):
			u = u 
		elif(v[i] == 4):
			u = u / 2
		i = i + 1
print(round(u, 2))
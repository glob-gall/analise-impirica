from numpy import *

mes = array(["janeiro", "fevereiro" ,"marco" ,"abril","maio",  "junho" ,"julho", "agosto" ,"setembro", "outubro" ,"novembro", "dezembro"])
data = input("data")

d = data[0:2]
m = ""
y = data[4:]
i = 0

while(i <=11):
	if(int(data[2:4]) - 1 ==i):
		m = mes[i]
	i= i+1
	
print(str(d)+" de "+ m+ " de " + str(y))
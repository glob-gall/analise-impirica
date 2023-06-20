from numpy import*

media_nota = array(eval(input()))
presenca = array(eval(input()))
carga_horaria = array(eval(input()))
vn = zeros(3,dtype = int)

for i in range(size(media_nota)):
	if(media_nota [i] >= 5) and (presenca[i] >= 0.75 * carga_horaria):
		vn[0] = vn[0] + 1
	elif(media_nota[i] <= 5) and (presenca[i] >= 0.75 * carga_horaria):
		vn[1] = vn[1] + 1
	else: 
		vn[2] = vn[2] + 1
print(vn)
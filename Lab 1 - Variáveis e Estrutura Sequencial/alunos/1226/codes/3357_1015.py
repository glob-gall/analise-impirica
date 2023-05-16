a= int(input("?"))
b= int(input("?"))
c= int(input("?"))
minimo=min(a,b,c)
maximo=max(a,b,c)

med= (a+b+c)-minimo-maximo
print(minimo)
print(med)
print(maximo)
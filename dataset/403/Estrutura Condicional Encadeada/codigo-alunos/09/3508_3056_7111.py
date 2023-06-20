A = float(input("Qual a area: "))

if (A>=0) and (A<10000):
    VT = (A*6) + 100
elif (A>10000) and (A<=20000):
    VT = (A * 5.50) + 150
elif (A>20000) and (A<=30000):
    VT = (A*5) + 200 
elif (A>30000):
    VT= (A*4.50) + 250 
print(round(VT,2))
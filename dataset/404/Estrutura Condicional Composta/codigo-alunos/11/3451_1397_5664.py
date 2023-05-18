area= float(input('area: '))

if area<=10000:
	custo=5*area
if area>10000:
	custo=5*10000+4*(area-10000)
print(custo)
		
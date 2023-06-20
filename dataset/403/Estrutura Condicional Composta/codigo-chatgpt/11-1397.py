area_fertilizada = float(input("Digite a área a ser fertilizada (em hectares): "))

if area_fertilizada <= 10000:
    custo_total = area_fertilizada * 5.00
else:
    custo_total = 10000 * 5.00 + (area_fertilizada - 10000) * 4.00

custo_total = round(custo_total, 2)
print("Valor total a ser cobrado: R$", custo_total)

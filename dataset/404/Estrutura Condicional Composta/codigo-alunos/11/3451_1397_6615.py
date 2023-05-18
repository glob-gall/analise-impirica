a = 10000.0
A = float(input("qual o tamanho da area a ser fertilizada: "))

b = (A-a)

if (A <= a):
	vtt1 = 5.00 * A
	print(round(vtt1,2))
else:
	vtt2 = 5*a + 4* b
	print(round(vtt2,2))
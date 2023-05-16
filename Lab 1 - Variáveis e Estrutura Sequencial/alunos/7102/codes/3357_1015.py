a = int(input())
b = int(input())
c = int(input())

ma = max(a,b,c)
mi = min(a,b,c)

so = a + b + c
me = so - (ma + mi)

print(mi)
print(me)
print(ma)
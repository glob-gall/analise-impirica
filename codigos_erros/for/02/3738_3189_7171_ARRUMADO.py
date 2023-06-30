import numpy as np

mf = np.array(eval(input()))
fq = np.array(eval(input()))
ch = float(input())

vet = np.zeros(3, dtype=int)
fqmin = ch * 0.75

ap = 0  # aprovado
rpn = 0  # rep. notas
rpf = 0  # rep. frequência

for i in range(np.size(mf)):
    if mf[i] >= 5 and fq[i] >= fqmin:
        ap += 1
        vet[0] = ap
    elif mf[i] < 5:
        rpn += 1
        vet[1] = rpn
    elif fq[i] < fqmin:
        rpf += 1
        vet[2] = rpf

print(vet)

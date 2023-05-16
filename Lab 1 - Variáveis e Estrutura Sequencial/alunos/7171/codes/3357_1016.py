# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.

from math import*

ent1= float( input( "Digite o comprimento dos lados do triangulo:"))
ent2= float( input())
ent3= float( input ())		
smptro= ((ent1 + ent2 +ent3) / 2)
area= round( sqrt(smptro*(smptro - ent1) * (smptro - ent2) * (smptro - ent3)), 5)
print( area)
				
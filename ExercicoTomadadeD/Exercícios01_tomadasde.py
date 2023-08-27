# 1Faça um Programa que peça dois números e imprima o maior deles#

n1 = int (input('entre com o Primeiro valor:'))
n2 = int (input('entre com o Segundo valor:'))

if n1 > n2:
    print(' O maior valor informado é : {0}'.format(n1))
elif n2 > n1:
    print(' O maior valor informado é : {0}'.format(n2))
else : 
    print()
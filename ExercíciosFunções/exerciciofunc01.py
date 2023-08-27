#Faça um programa,com uma função que necessite de três argumentos,e que forneça a soma desses três argumentos.

def soma(a,b,c):
    resulatdo = a+b+c
    return resulatdo
   

n1= int(input('informe o Primeiro valor:'))
n2= int(input('informe o Segundo valor:'))
n3= int(input('informe o Terceiro valor:'))

resposta = soma(n1,n2,n3)
print(f'a soma entre os valore é :{resposta}') 

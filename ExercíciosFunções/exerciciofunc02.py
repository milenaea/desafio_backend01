# Reverso do número.Faça uma função que retorne o reverso de um número inteiro informado.Porexemplo:127->721.



def reverso_numero(n):
    return int(str(n)[::-1])

n1 = int(input('Informe um valor inteiro: '))
n1_reverso = reverso_numero(n1)
print('O valor invertido é:', n1_reverso)
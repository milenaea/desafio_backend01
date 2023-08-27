#Faça um programa que peça uma nota,entre zero e dez. Mostre uma mensagem caso o valor seja
# inválido e continue pedindo até que o usuário informe um valor válido.

nota = 11

while (nota <0) or (nota >10):
    nota = float(input('Informe sua Nota:'))
    if(nota >=0) and (nota<=10):
        print('NOta Valida')
    else:
        print("Valor Invalido!")
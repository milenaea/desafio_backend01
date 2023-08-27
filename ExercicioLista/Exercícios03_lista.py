#Escreva um programa em Python que onde todos os  valores em um dicionário são 
#emitidos. Se sim, imprima True.Caso contrário,imprima Falso


dicionario = { 'chave':'valor',
              'chave1': None,
              'chave2':'valor2'}
for chave, valor in dicionario.items():
    print(chave)
    print(valor)
    if (valor == '') or (valor == None):
        print(False)
    else:
        print (True)
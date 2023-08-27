#2.Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.
#Imprima a mensagem "BomDia!","BoaTarde!"ou"BoaNoite!"ou"Valor Inválido!",conformeocaso.#

periodo = input('Informe o turno em que você estuda, M-matutino ou V-Vespertino ou N-Noturno: ')
if periodo.upper() == "M":
    print('BomDia!')
elif periodo.upper() == "V":
    print('BOa TArde!')
elif periodo.upper() == "N":
    print('Boa NOite!')
else:
    print('INVALIDO')
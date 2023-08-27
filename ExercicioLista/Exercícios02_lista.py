#02.Programa nome ao contrário em maiúsculas.
#Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário 
#de trás para frente utilizando somente letras maiúsculas.
#Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.


entrada = (input('informe seu nome:'))
entrada_maior = entrada.upper()
texto_invertido =''.join(reversed(entrada_maior))
print('O texto invertido é: ', texto_invertido)
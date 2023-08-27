lista_perguntas = []
lista_perguntas.append('Telefonou para a vítima?')
lista_perguntas.append('Esteve no local do crime?')
lista_perguntas.append('Mora perto da vítima??')
lista_perguntas.append('Devia para a vitima?')
lista_perguntas.append('Já trabalhou com a vítima?')

contagem=0

for pergunta in lista_perguntas:
    print(pergunta) 
    resposta = int(input('Informe a respostas ( usando 1 = sim e 0 = não) :'))

    if resposta==1:
        contagem = contagem + 1

print(contagem)
if contagem == 2:
    print('Suspeita')

elif (contagem >= 3) and (contagem <5): 
    print('Cúmplice')

elif contagem >=5:
    print('Assassino!')

else:
    print('INOCENTE!')
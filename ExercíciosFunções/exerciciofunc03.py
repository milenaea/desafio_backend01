#03.Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de grauCelsius para Fahrenheit ou vice-versa.
#Para cada opção,crie uma função.Crie uma terceira,que é um menu para o usuário escolher a opção desejada,
#onde esse menu chama a função de conversão correta.

'''ceucius = float(input('entre com o valor da temperatura em ceucius: '))
conversao = ceucius * 1.8 +32
print(conversao)'''

'''periodo = input('Informe o turno em que você estuda, M-matutino ou V-Vespertino ou N-Noturno: ')
if periodo.upper() == "M":
    print('BomDia!')
elif periodo.upper() == "V":
    print('BOa TArde!')
elif periodo.upper() == "N":
    print('Boa NOite!')
else:
    print('INVALIDO')'''

tipo_op = int(input(' Entre com \n 1 para trasnformar Celsius em Fahrenheit \n 2 para transformar Fahrenheit em Celsius :'))
temperatura = float(input(' Digite a temperatura:')) 
if tipo_op == 1:
    resultado = temperatura * 1.8 +32
    print(f"resultado da conversão: {resultado} Fahrenheit ")
elif tipo_op ==2:
    resultado =  (temperatura - 32) * 5/9 

    print(f"resultado da conversão: {resultado} Celsius")
else:
    print('Tipo da Operação não Permitida!')
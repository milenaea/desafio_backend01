#01. Faça um Programa que peça as quatro notas de 10 alunos,
#calcule e armazene numa lista a média de cada aluno,imprima o número de alunos commédia maior ou igual a 7.0

medias_alunos = []
for i in range(0, 10):
    print(f"Aluno {i}")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    #print(media)
    medias_alunos.append(media)
#print(medias_alunos)
for x in medias_alunos:
        if(x) >=7:
            print('As medias acima de 7.0 são:')
            print(x)
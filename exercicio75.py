#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
alunos=[]
alunomaior=0
for c in range(0,3):
    aluno=str(input('Digite o nome do aluno: '))
    nota1=float(input('Digite a nota 1: '))
    nota2=float(input('Digite a nota 2: '))
    nota3=float(input('Digite a nota 3: '))
    nota4=float(input('Digite a nota 4: '))
    media=(nota1+nota2+nota3+nota4)/4
    if media>=7.0:
        alunomaior+=1
    alunos.append([[aluno],[media]])
print('=-'*30)
for c in alunos:
    print(f'ALUNO: {c[0]}, MÉDIA: {c[1]}')

print(f'NÚMERO DE ALUNOS APROVADOS: {alunomaior}')


#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
aluno=[]
while True:
    nome=str(input('Digite o nome do aluno: '))
    nota1=float(input('Digite a nota 1: '))
    nota2=float(input('Digite a nota 2: '))
    nota3=float(input('Digite a nota 3: '))
    nota4=float(input('Digite a nota 4: '))
    media=(nota1+nota2+nota3+nota4)/4
    if media>=6:
        apv='APROVADO'
    else: 
        apv='REPROVADO'
    aluno.append([nome,[nota1,nota2,nota3,nota4],media,apv])
    rp=str(input('Quer continuar? [S/N] ')).upper()
    if rp in 'N':
        break
print('##'*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}{"RESULTADO":>12}')
print('-'*35)
for i,n in enumerate(aluno):
    print(f'{i:<4}{n[0]:<10}{n[2]:>8}{n[3]:>12}')
while True:
    pert=int(input('Digite o número do aluno para ver a nota:[999 para interromper] '))
    if pert==999:
        print('FINALIZANDO O PROGRAMA')
        break
    if pert<=len(aluno)-1:
        print(f'As notas de aluno {aluno[pert][0]} são: {aluno[pert][1]}')
#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
notas=[]
while True:
    nota1=float(input('Digite a nota 1: '))
    nota2=float(input('Digite a nota 2: '))
    nota3=float(input('Digite a nota 3: '))
    nota4=float(input('Digite a nota 4: '))
    media=(nota1+nota2+nota3+nota4)/4
    notas.append([[nota1,nota2,nota3,nota4],media])
    resp=str(input('Deseja continuar? [S/N]')).upper()
    if resp in 'Nn':
        break
print(f'{"NOTAS":<8}{"MÉDIA":>25}')
for c in notas:
    print('{}{:>12}'.format(c[0],c[1]))
    
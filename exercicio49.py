''' Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. '''
print('¬¬¬¬'*5)
print(' CADASTRO DE PESSOAS')
print('¬¬¬¬'*5)
maior=0
homi=0
moca=0
while True:
    age=int(input('Digite a idade: '))
    sexo=' '
    while sexo not in 'FM':
        sexo=str(input('Digite o sexo [M/F]: ')).upper()
    if age>18:
        maior+=1
    if sexo=='M':
        homi+=1
    if sexo=='M':
        if age<20:
            moca+=1
    cont=' '
    while cont not in 'SN':
        cont=str(input('Você deseja continuar? [S/N]')).upper()
    if cont=='N':
        break
print(f'maior de idade {maior}')
print(f'homens cadastrados {homi}')
print(f'mulheres menor {moca}')
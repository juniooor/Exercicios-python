'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
pessoa={}
grupo=[]
soma=media=0
grupoG=[]
while True:
    pessoa.clear()
    pessoa['nome']=str(input('Nome?: '))
    while True:
        pessoa['sexo']=str(input('Sexo?: [M/F]')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('Digite apenas [M] ou [F]')
    pessoa['idade']=int(input('Idade: '))
    soma+=pessoa['idade']
    grupo.append(pessoa.copy())
    while True:
        r=str(input('Deseja continuar? [S/N]')).upper()
        if r in 'SN':
            break
        print('responda apenas [S] ou [N]')
    if r=='N':
        break
print('///'*25)
print(f'foram cadastradas {len(grupo)} pessoas') #quantas pessoas tem no gp
media=soma/len(grupo)
print(f' a média de idade é:  {media:.3f} Anos')
print(f'AS mulheres cadastradas foram',end=' ')
for p in grupo:
    if p['sexo'] == 'F':
        print(f',{p["nome"]}',end='')
    print()
print('As pessoas acima da media foram: ')
for p in grupo:
    if p['idade']>media:
        print(' ',end='')
        for k,v in p.items():
            print(f'{k} = {v};',end='')
        print()
print('<<<FINALIZANDO>>>')
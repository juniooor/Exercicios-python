''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.'''

'''
date=[]
peaple=[]
pesomaior=[]
pesomenor=[]
while True:
    peaple.append(str(input('Digite o nome da pessoa: ')))
    peaple.append(float(input('Digite o peso: (kg)')))
    date.append(date[:])
    peaple.clear()
    r=str(input('Deseja continuar? [S/N]')).upper()
    if r in 'N':
        break
for p in date:
    #if p[1]>=85:
     #   pesomaior.append(p[0])
    if p[1]<=60:
        pesomenor.append(p[0])        
print(f'foram cadastradas {len(date)} pessoas')
print(f'As pessoas com mais de 85kg foram: {pesomaior}')
print(f'As pessoas com menos de 60kg foram: {pesomenor}')
print({}.format('Fim do programa'))'''


maior=menor=0
galera=[]
dado=[]
psup=[]
pinf=[]
while True:
    dado.append(str(input('Qual o nome?: ')))
    dado.append(float(input('QUal o peso?: ')))
   # dado.append(str(input('Qual o sexo?: [M/F]').upper()))
    galera.append(dado[:])
    dado.clear()
    r=str(input('Quer continuar? [S/N]')).upper()
    if r in 'nN':
       break 
for p in galera:
    if p[1]>=85:
        psup.append(p[0])
        maior+=1
    elif p[1]<=50:
        pinf.append(p[0])
        menor+=1
print(f'foram cadastradas {len(galera)} pessoas')
print(f'As pessoas com menos de 50kg foram {pinf}')
print(f'As pessoas com mais de 85kg foram {psup}')

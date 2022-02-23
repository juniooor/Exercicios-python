#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes
palavras=[]
cont=0
palavras.append(str(input('Digite uma palavra até 10 caracteres desconsiderendo acentuação: ')))
for p in palavras:
    print(f'\nA palavra "{p}" tem: ',end='')
    for letra in p:
        if letra.lower() in 'bcdfghjklmnpqrstvwxz':
            print(letra,end=' ')
            cont+=1
    print(f'tem {cont} consoantes')
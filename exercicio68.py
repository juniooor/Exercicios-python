# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

print('==='*15)
print('             PALPITES MEGA-SENA')
print('==='*15)
lista=[]
jogos=[]
jogo=int(input('Quantos jogos vocÊ vai apostar?: '))
tot=1
while tot <=jogo:
    cont=0
    while True:
        num=randint(1,60)
        if num not in lista:
            lista.append(num)
            cont+=1
        if cont>=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(f'Sorteando {jogo} jogos!! ')
for i,l in enumerate(jogos):
    print(f'jogo {i+1}: {l}')

print('Se ganhar com esses números quero 30% do prêmio. BOA SORTE!!')
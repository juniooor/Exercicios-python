'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada'''

def contador(inicio,fim,passo=1):
    if passo==0:
        passo=1
    for n in range(inicio,fim, passo):
        print(n,end=' ')
    print()

contador(1,10, 1)
contador(10,0, -2)
i=int(input('Digite o valor de inicio: '))
f=int(input('Digite o valor final: '))
p=int(input('Digite o passo: '))
contador(i,f,p)
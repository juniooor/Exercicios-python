'''#Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''
from time import sleep
op=0
print('OPERAÇÕES E MENU')
n1=int(input('Digite o primeiro valor: '))
n2=int(input('Digite o segundo valor: '))
while op !=5:
    sleep(1)
    op=int(input('DIGITE \n [1]SOMA:  \n [2]MULTIPLICAR:   \n [3]MAIOR NÚMERO:  \n [4]DIGITAR NOVOS NÚMEROS:  \n [5]SAIR DO PROGRAMA: '))
    if op==1:
        print('A soma dos números {}+{}={}'.format(n1,n2,(n1+n2)))
    elif op==2:
        tot=n1*n2
        print('A multiplicação dos números {}x{}={}'.format(n1,n2,tot))
    elif op==3:
        if n1>n2:
            print('O Maior número é: {}'.format(n1))
        else:
            print('O Maior número é: {}'.format(n2))
    elif op==4:
        n1=int(input('Digite o primeiro valor: '))
        n2=int(input('Digite o segundo valor: '))
    elif op==5:
        print('Retornando ao Menu')
        sleep(1)


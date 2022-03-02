'''Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.'''
print('-----DESAFIO 99-----')
def fot(n):
    for i in range(1,n+1):
        print((str(i)+" ")*i)

x=int(input('número: '))


'''Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.'''
print('-----DESAFIO 100-----')
def imprimir(valor):
    if isinstance(valor, int):
        x = 1
        while x <= valor:
            y = 1
            texto=''
            while y <= x:                
                texto += str(y) + ' '
                y += 1
            print (texto)
            x += 1

x=int(input("numero: "))
imprimir(x)
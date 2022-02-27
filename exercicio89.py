#aça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
print('CALCULADORA DE AREA DE TERRENO')

def area(a, b):
    ar=a*b
    print(f'A àrea do terreno {a} x {b} é de {ar}m²')


larg=float(input('largura do terreno: '))
comp=float(input('Comprimento do terreno: '))
area(larg,comp)
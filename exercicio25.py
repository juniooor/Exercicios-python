#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

r1=int(input('Digite a reta 1: '))
r2=int(input('Digite a reta 2: '))
r3=int(input('Digite a reta 3: '))
if r1+r2>+r3 and r2+r3>+r1 and r1+r3>=r2:
    print('As medidas {},{} e {}, Podem se tornar um triangulo: '.format(r1,r2,r3))
    if r1==r2==r3:
        print('EQUILATÉRO')
    elif r1==r2 or r2==r3 or r3==r1:
        print('ISOSCÉLES')
    elif r1!=r2 and r2!=r3 and r3!=r1:
        print('ESCALENO')
else:
    print(' os seguimentos digitados não podem formar um triangulo')
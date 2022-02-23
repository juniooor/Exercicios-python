#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os número.
import numpy
vetor=[]
for n in range(0,5):
    valor=int(input(f'digite o {n+1} valor: '))
    vetor.append(valor)
soma=sum(vetor)
mult=numpy.prod(vetor)
print('-=-'*20)
print(f'A soma dos números: {soma}')
print(f'A multiplicação dos números: {mult}')
print(f'Os números foram: {vetor}')
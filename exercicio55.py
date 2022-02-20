'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
cont=0
lista=(int(input('Digite um numero: ')),int(input('Digite um número: ')),int(input('Digite um número: ')),int(input(('Digite um número: '))))
print(f'Você digitou os numeros: {lista}')
if 3 in lista:
    print(f'O numero 3 foi digitado na posição {lista.index(3)+1}')
else:
    print('O número 3 nao foi registrado')
if 9 in lista:
    print(f'O número 9 foi digitado {lista.count(9)} Vezes')
else:
    print('o Número 9 não foi registrado')
print('O numeros pares foram: ') 
for n in lista:
    if n %2==0:
        print(f'{n}', end=' ')
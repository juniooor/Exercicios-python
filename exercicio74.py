#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
num=[[],[]]
for n in range(1,20):
    numero=int(input(f'Digite o {n}º número: '))
    if numero%2==0:
        num[0].append(numero)
    elif numero%2==1:
        num[1].append(numero)
print(f'Os numeros digitados foram: {num}')
print(f'Os números pares foram: {num[0]}')
print(f'Os números impares foram: {num[1]}')
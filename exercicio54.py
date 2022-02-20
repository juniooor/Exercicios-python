# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint


lista=(randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
print(f'Os numeros gerados foram: {lista}')
print(f'O maior valor é {max(lista)}')
print(f'O menor valor é {min(list)}')
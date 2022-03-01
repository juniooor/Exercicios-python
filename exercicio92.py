#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    maximo=max(num)
    print(f'dos numeros {num}',end=' ')
    print(f'foram informados {len(num)}')
    print(f"O maior número é {maximo}")


maior(1,6,8,9,5,4,2)

maior(6,5,3,7)

maior(0)

maior(4,2,1)

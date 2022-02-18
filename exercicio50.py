''' Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. '''
print('~~~'*7)
print('MERCADINHO DO JUNIOR')
print('~~~'*7)
soma=maior=menor=contador=0
menorp=' '
while True:
    produto=str(input('Nome do produto: '))
    valor=float(input('Valor do produto: '))
    contador +=1
    soma+=valor
    if valor>1000:
        maior+=1
    if contador==1 or valor<menor:
        menor=valor
        menorp=produto
    cont=str(input('Deseja continuar? [S/N]: ')).upper()
    if cont=='N':
        break
print('{:-^40}'.format(' RESUMO DOS PRODUTOS '))
print(f'total de R${soma:.2f}')
if maior>=1:
    print(f'{maior} produto(s) maior que R$1000,00')
else:
    print('não teve produtos maiores que R$1000,00')
print(f'O produto mais barato é {menorp} , que custou R${menor:.2f}')
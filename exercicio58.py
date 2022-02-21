#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 


valor=[]
for cont in range(0,5):
    valor.append(int(input(f'Digite o {cont} valor: ')))
    cont+=1
print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} nas Posições',end=' ')
for c,v in enumerate(valor):
    if v==max(valor):
        print(f'{c}...', end='')
print(f'\n O menor valor digitado foi {min(valor)} nas posições', end=' ')
for c,v in enumerate(valor):
    if v==min(valor):
        print(f'{c}...',end='')

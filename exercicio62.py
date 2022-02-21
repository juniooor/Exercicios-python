''' Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.'''
a=[]
while True:
    a.append(int(input('Digite um valor: ')))
    r=str(input('Quer Continuar? [S/N]')).upper()
    if r in 'N':
        break
print(f'A lista completa é: {a}')
b=[]
c=[]
for n in a:
    if n%2==0:
       b.append(n)
    else:
        c.append(n)        
print(f'A lista de numeros pares: {b}')
print(f'A Lista de numeros impares: {c}')
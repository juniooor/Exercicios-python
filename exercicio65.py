#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
num=[[],[]]
for n in range(0,7):
    nume=(int(input(f'Digite o {n}º numero: ')))
    if nume%2==0:
        num[0].append(nume)
    else:
        num[1].append(nume)
num[1].sort()
num[0].sort()
print(f'numeros pares {num[0]}')
print(f'Numeros impares {num[1]}')

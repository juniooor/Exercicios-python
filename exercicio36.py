#Faça um programa que leia o peso de 5 pessoas. no final mostre qual foi o maior e o menor peso lidos
high=0
low=0
for people in range(1,6):
    peso=float(input('Digite o peso da {}º Pessoa: '.format(people)))
    if people==1:
        high=peso
        low=peso
    else:
        if peso>high:
            high=peso
        if peso<low:
            low=peso
print('o Maior peso foi de {}kg'.format(high))
print('O Menor peso foi de {}kg'.format(low))
from re import S


print('calcule quanto você ganha por mês: ')
s = float(input('Quanto você ganha por hora?: '))
h= float(input('Quantas horas você trabalha por mês?: '))
print(' você ganha R${} por mês'.format(s*h))

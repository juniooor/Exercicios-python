# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
print('10 TERMOS DE UMA P.A')
raz=int(input('RAZÃO:\t'))
termo=int(input('TERMO:\t'))
dez=termo+(11-1)*raz
for c in range(termo,dez, raz):
    print(c, end=' ')
print('FIM')
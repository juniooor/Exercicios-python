#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 
from calendar import c


print('TABÚADA')
while True:
    n=int(input('Digite um número para mostrar sua tabúada ou um número negativo para finalizar: '))
    if n<0:
        break
    c=0
    cont=0
    while c<=10:
        r=n*c
        print(f'{n}x{c}={r}')
        c+=1   
print('PROGRAMA DESATIVADO, OBRIGADO POR USAR')
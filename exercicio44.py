#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

print('SOMA DE VALORES')
cont=0
n=1
soma=0
while n!=999:
    n=int(input('Digite o valor: '))
    if n !=999:
        cont+=1
        soma=soma+n
    else:
        print('somando')
        
        
print(' foram digitados {} numeros e a soma dos numeros foi {}'.format(cont,soma))
    
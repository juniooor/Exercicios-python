#Faça um programa que leia um número qualquer e mostre o seu fatorial.



count=1
tot=1
c='S'
while c !='N':
    f=int(input('Digite um número para mostar o seu fatorial: '))
    while count<=f:
        tot*=count
        count+=1
    print('resultado é {}'.format(tot))
    c=str(input('Deseja Continuar?: [S/N]')).upper()
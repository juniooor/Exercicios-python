#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('10 TERMOS DE UMA PA')
termo=int(input('TERMO: '))
raz=int(input('Razão: '))
cont=1
tot=0
mais=10
while mais !=0:
    tot+=mais
    while cont<=tot:
        print('pa {}'.format(termo))
        cont+=1
        termo+=raz
    mais=int(input('deseja ver mais termos?'))
print('fim')
    


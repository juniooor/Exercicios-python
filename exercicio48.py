#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 
from random import randint

print('JOGO PAR OU IMPAR')
v=0
while True:
    ply=int(input('Digite um valor: '))
    pc=randint(1,10)
    soma=ply+pc
    tipo=' '
    while tipo not in 'PI' :
        tipo=str(input('VOCÊ ESCOLHE PAR OU IMPAR? [P/I]')).upper()
    print(f'Você jogou {ply} e o Computador jogou {pc} A soma foi {soma}')
    print('DEU PAR'if soma%2==0 else 'DEU IMPAR' )
    if tipo=='P':
        if soma%2==0:
            print('Você ganhou!!')
            v+=1
        else:
            print('Você perdeu!!')
            break
    elif tipo=='I':
        if soma%2==1:
            print('Você venceu!!')
            v+=1
        else:
            print('Você perdeu!!')
            break   
    print('Vamos jogar novamente :D')
print(f'FIM DE JOGO!!. VOCÊ GANHOU {v} VEZ(ES)!! ')

# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
contchute=0
print('¬¬¬'*7)
print(' JOGO DE ADVINHAÇÃO')
print('¬¬¬'*7)
print('Irei pensar em um número de 1 até 10, e você tentará acertar')
num=randint(1,10)
chute=int(input('chute um número: '))
contchute+=1
if chute==num:
    print('uau acertou de primeira')
else:
    print('infelizmente errou, dessa vez vou dá uma dica')
    while chute!=num:
        chute=int(input('tente novamente,qual número eu estou pensando?: '))
        contchute+=1
        if chute<num:
            print('chute mais alto')
        else:
            print('chute mais baixo')
    print('você chutou {} vezes, o número que eu pensei foi {}'.format(contchute,num))

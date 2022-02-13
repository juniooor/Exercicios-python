# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens= ('pedra', 'papel', 'tesoura')
pc= randint(0,2)

print('vamos jogar jokepô')
player =int(input('escolha entre: \n [0]Pedra \n [1]Papel \n [2]Tesoura'))
print('¬¬¬¬'*8)
print('    O computador jogou {}'.format(itens[pc]))
print('    O jogador jogou {}'.format(itens[player]))
print('¬¬¬¬'*8)
if player==0:
    if pc==0:
        print('====EMPATE====')      
    elif pc==1:
        print('====COMPUTADOR VENCEU====')
    elif pc==2:
        print('====JOGADOR VENCEU====')
    else:
        print('JOGADA INVÁLIDA')
elif player== 1:
    if pc==0:
        print('====JOGADOR VENCEU====')
    elif pc==1:
        print('====EMPATE====')
    elif pc==2:
        print('====COMPUTADOR VENCEU====')
    else:
        print('JOGADA INVÁLIDA')
elif player == 2:
    if pc == 0:
        print('====COMPUTADOR VENCEU====')
    elif pc == 1:
        print('====JOGADOR VENCEU====')
    elif pc == 2:
        print('====EMPATE====')
    else:
        print('JOGADA INVÁLIDA!')
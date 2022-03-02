# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(j='',g=''):
    if j=='':
        j='<Desconhecido>'
    if not g.isdigit():
        g=0
    return f'O Jogador {j} fez {g} Gol(s) no campeonato'


jog=str(input('Nome: '))
gol=str(input('gols: '))
print(ficha(jog,gol))
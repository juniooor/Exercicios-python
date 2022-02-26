#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter
jogadores={'jogador1':randint(1,6),'jogador2':randint(1,6),'jogador3':randint(1,6),'jogador4':randint(1,6)}
for k,i in jogadores.items():
    print(f'o {k} tirou : {i}')
    sleep(1.2)
ranking={}
ranking=sorted(jogadores.items(),key=itemgetter(1),reverse=True)
print('_=_'*20)
print('RESULTADO')
for i,k in enumerate(ranking):
    print(f' Em {i+1}º lugar o {k[0]} com {k[1]} Pontos.')
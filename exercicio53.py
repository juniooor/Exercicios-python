''' Crie uma tupla preenchida com os 22 primeiros colocados da Tabela das olimpiadas de inverno 2022, na ordem de colocação. Depois mostre:
a) Os 5 primeiros paises.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o canadá.'''
from time import sleep


tabela=('Noruega','Alemanha','Estados Unidos','China','Holanda','Suécia','Suiça','Áustria','Comitê Russo','França','Canadá','Japão','Itália','Coreia do Sul','Eslováquia','Bielorrússia','Espanha','Ucrânia','Bélgica','Estônia','Letônia','Polônia')
print('Os 5 primeiros paises são {} '.format(tabela[0:5]))
sleep(1)
print('-'*70)
print('Os ultimos 4 colocados são: {}'.format(tabela[-4:]))
sleep(1)
print('-'*70)
print(f'Os Paises em ordem alfabetica: \n {sorted(tabela)}')
sleep(1)
print('-'*70)
print('O Canadá está na posição {}º das Olimpiadas'.format(tabela.index('Canadá')+1))
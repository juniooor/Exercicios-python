
from datetime import date, datetime
print('========'*5)
print('   ANALISE DE PESSOAS MAIORES DE IDADE')
print('========'*5)
atual=date.today().year
gusmenor=0
gusmaior=0
for c in range(1,8):
    ano=int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade=atual - ano
    if idade>=21:
        gusmaior+=1
    else:
        gusmenor+=1
print('Tem {} pessoas Maior de idade \n Tem {} pessoas Menores de idade.'.format(gusmaior,gusmenor))
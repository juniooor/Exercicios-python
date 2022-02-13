
from datetime import datetime


print('------'*5)
print('Digite seu ano de nascimento para saber se deve se alistar nas forças armadas')
print('------'*5)
year=int(input('Digite seu ano de nascimento: '))

time=2022-year
if time>18:
    atr=time-18
    print('você está {} anos atrasado, siga para a junta militar mais proxima'.format(atr))
elif time<18:
    tmp=18-time
    print('falta {} ano(s) para você se alistar. siga para a junta militar mais proxima'.format(tmp))
else:
    print('Você já pode se alistar, siga para a junta militar mais proxima')
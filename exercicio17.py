#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 #situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de #folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math


print('Programa para realizar o calculo de quantas latas precisa ')
area=int(input('Quantos metros quadrados vão ser pintados?: '))
litros=(area/6)*1.1
latas=math.ceil(litros/18)
valorl=latas*80
galao=math.ceil(litros/3.6)
valorg=galao*25

mislata= round(litros/18)
misgalao= round((litros-mislata *18)/3.6)
if((litros-(mislata*80)%3.6 !=0)):
    misgalao+=1
    totalmis= (mislata*80)+(misgalao*25)
    print('Para compras em latas será necessario {} Latas, que irão custar R${:.2f}'.format(latas,valorl))
    print('Para Compras em galoes são necessario {} que irão custar R${:.2f}'.format(galao,valorg))
    print('para evitar perdas você pode comprar {} galoes e {}latas, que irá custar {}'.format(misgalao,mislata,totalmis))
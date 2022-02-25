#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

ano=[['janeiro'],['fervereiro'],['março']]
temp=[]
acimamedia={}
#meses={'1':'janeiro','2':'fervereiro','3':'março','4':'abril','5':'maio','6':'junho','7':'julho','8':'agosto','9':'setembro','10':'outubro','11':'novembro','12':'dezembro'}
for m in ano:
    temp.append(float(input(f'Qual a temperatura do mês de {m}?: ')))
  
media=sum(temp)/len(ano)

for i in ano:
 	if(temp[i] > media):
 		acimamedia={ano[i] : temp[i]}
print(f'media da temperatura trimestral: {media:.1f}')
print(f'mes(es) com temperatuda acima da média: {acimamedia}' )


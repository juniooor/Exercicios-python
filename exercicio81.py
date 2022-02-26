#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

ano=[['janeiro'],['fervereiro'],['março'],['abril'],['maio'],['junho'],['julho']]
temp=[]
meses_acima=()
mes=[]
for m in ano:
    temp.append(float(input(f'Qual a temperatura do mês de {m}?: ')))
#faço a soma de todas as temperaturas,e divido pelo numeros de meses no ano
media=sum(temp)/len(ano)
#percorro toda a lista de ano e temperatura para identificar a temperatura e o mes que ocorreu a maior taxa
for i in range(len(ano)):
	if(temp[i] > media):
		meses_acima=(ano[i],temp[i]) #criei a tupla para armazenar os dados dos meses com temperatura maior
		mes.append(meses_acima) #e a lista para mostrar todos os dados...
print(f'media da temperatura semestral: {media:.1f}')
print(f'mes(es) com temperatuda acima da média: {mes}' )


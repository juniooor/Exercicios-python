temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
acimaMedia = {}
for i in range(len(meses)):
    temperatura.append(float(input(f'Informe a Temperatura media de {meses[i]} :\n')))

media= sum(temperatura)/len(meses)

for i in range(len(meses)):
 	if(temperatura[i] > media):
 		acimaMedia.update({meses[i] : temperatura[i]})


print(f'Media das temperaturas : Anual -> {media}')
print(f'Meses com temperaturas acima da media: {acimaMedia}')
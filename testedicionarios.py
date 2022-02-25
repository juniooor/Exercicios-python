'''pessoas={'nome':'Júnior','idade':'21','sexo':'M'}
print(pessoas['idade'])
print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

#para cada uma das chaves
for k in pessoas.values():
    print(k)
del pessoas['sexo'] #deletar elemento
pessoas['nome']='vini' #modifica um elemento
pessoas['peso']=61.2
for k,v in pessoas.items():
    print(f'{k}={v}')

#CRIAR UM DICIONARIO DENTRO DE UMA LISTA

marca=[]
model1={'honda':'Civic'}
model2={'honda':'Fit'}
marca.append(model1)
marca.append(model2)

print(marca)'''

estado={}
brasil=[]

for c in range(0,3):
    estado['uf']=str(input('Unidade federativa: '))
    estado['sigla']=str(input('sigla do estado: '))
    brasil.append(estado.copy())

for n in brasil:
    for k,v in n.items():
        print(f'o campo {k} tem valor {v}')
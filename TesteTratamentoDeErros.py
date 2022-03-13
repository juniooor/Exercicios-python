'''conjut= {1,2,3,4}
print(type(conjut))'''

conjuto1= {1,2,3,4,5}
conjuto2={5,6,7,8}

conjutouniao=conjuto1.union(conjuto2) #Faz a união entre dois conjuntos e remove duplicidade
print(conjutouniao)
conjutointesecção= conjuto1.intersection(conjuto2) #mostrar o que tem de igual nos dois conjuntos
print(conjutointesecção)
conjutodiferente1=conjuto2.difference(conjuto1) #mostra a diferença de um conjunto para o outro
conjutodiferente2=conjuto1.difference(conjuto2)
print(conjutodiferente1)
print(conjutodiferente2)
conjut_diff_asimetrica = conjuto1.symmetric_difference(conjuto2) #mostra a diferença entre os dois conjutos 
#ex: c1{1,2,3,5}  c2={1,2,3,4} => ele vai apenas mostrar o 5 e 4 porque é o que tem de diferente entre os conjutos
print(conjut_diff_asimetrica)


lista= ['cachorro','vaca','boi','gato','gato','rato']  #removendo duplicidade
connjuto_pet= set(lista)
print(connjuto_pet)
lista_pet= list(connjuto_pet)
print(lista_pet)
print(lista)
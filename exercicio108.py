#crie uma função para mostrar o maior valor par de uma lista



lista=[2,8,4,10,12,3,5,7] #Criei uma lista com vairos numeros

def maiorpar(lista): #dentro da função criei uma variavel chamada lista(tanto faz o nome)
    listapar=[]   #DENTRO DA FUNÇÃO criei uma lista para recolher os numeros pares da lista(variavel)
    for i in lista: #para cada i(numero) da lista
        if i%2==0: #se o i(numero) for dividio por 2=0 
            listapar.append(i) #adciona ele na lista de par
    return max(listapar) #no final o return retorna o MAX(maior) valor da lista par 



x=maiorpar(lista) #o X recebe o return da função
print(x)

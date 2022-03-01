#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteio(lista):
    for cont in range(0,6): #gerando 6 numeros
        lista.append(randint(0,10))   #a cada numero gerado ele é sorteado pelo randint que gera um valor de 0 a 10 
    print(lista)   


def somapar(lista):
    pares=[] #criado uma lista para armazenar os pares
    for n in lista: #para cada 'n' numero da lista 
        if n%2==0: #se n dividio por 2 for igual a 0 
            pares.append(n)  #adciona N na lista par
    soma=sum(pares) #sum é usado para somar a lista de par
    print(f'a lista {lista} é igual a {soma}')
            


#aqui é a o programa principal 
numbers=[] 
sorteio(numbers)
somapar(numbers)   
#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
lista=[]
for c in range(0,5):
    l=int(input('Digite um numero: '))
    if c==0 or l>lista[-1]:
        lista.append(l)
    else:
        pos=0
        while pos<len(lista):
            if l<=lista[pos]:
                lista.insert(pos, l)
                break
            pos+=1
print(f'Os valores da lista foram {lista}')
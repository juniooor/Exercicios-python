#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
lista=[]
for c in range(0,10):
    lista.append(float(input(f'Digite o {c}º numero real: ')))
lista.reverse()
print(lista)
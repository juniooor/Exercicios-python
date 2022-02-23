#Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
lista=[]
for c in range(0,5):
    lista.append(int(input(f'Digite o {c+1}º número: ')))
print('=-'*20)
for i in lista:
    print(i)
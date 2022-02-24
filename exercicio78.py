#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
vetora=[]
s=0
for c in range(0,10):
    valor=int(input(f'Digite o {c+1}º valor: '))
    vetora.append(valor)
for c in vetora:
    r=c**2
    s+=r
print(s)
    
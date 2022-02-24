#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade=[]
altura=[]
for c in range(0,5):
    age=(int(input('Digite a idade: ')))
    high=float(input('Digite a altura: '))
    idade.append(age)
    altura.append(high)
print('FORMA LIDA:')
print(idade)
print(altura)
print('=-'*20)
idade.reverse()
altura.reverse()
print('FORMA INVERSA:')
print(idade)
print(altura)
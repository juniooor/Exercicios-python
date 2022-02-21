'''num=[2,5,9,1]
num[2]=3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
#num.pop(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o numero 4')
print(num)
print(f'tem {len(num)} elementos')
print()'''
valor=[]
for cont in range(0,5):
    valor.append(int(input(f'Digite o valor {cont}: ')))
for c,v in enumerate(valor):
    print(f'na posição {c} temos o {v}!!')
#lista=[1,2,5,2,9,2,7,]


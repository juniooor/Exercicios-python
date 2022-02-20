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
valor.append(1)
valor.append(9)
valor.append(5)
valor.append(4)
for c,v in enumerate(valor):
    print(f'na posição {c} achei {v} valor')

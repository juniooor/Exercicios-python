lista=[]
vproduto=[]
nproduto=[]
for n in range(1,3):
    vprodut=float(input('Valor do produto: '))
    vproduto.append(vprodut)
    nprodut=str(input('Nome do produto:'))
    nproduto.append(nprodut)
    lista.append(vproduto[:])
    lista.append(nproduto[:])
    vproduto.clear()
    nproduto.clear()
print(lista)
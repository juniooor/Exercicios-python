soma=0
cont=0
for c in range(1,7):
    num=int(input('Digite o {}º valor: '.format(c)))
    if num % 2==0:
        soma+=num
        cont+=1
print('dos 6 numeros.{} são pares e a soma é {}'.format(cont,soma))
        
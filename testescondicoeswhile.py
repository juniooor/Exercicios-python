n=1
par=impar=0
while n != 0:
   n=int(input('Digite um valor: [DIGITE "0" PARA PARAR] '))
   if n !=0:
       if n%2==0:
           par+=1
       else:
            impar+=1
print('tem {} pares e {} impares'.format(par,impar))
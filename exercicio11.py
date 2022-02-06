n1=int(input('Digite o primeiro numero inteiro: '))
n2=int(input('Digite o segundo numero inteiro: '))
n3=float(input('Digite um numero real: '))
#o produto do dobro do primeiro com metade do segundo
a=n1*2/n2
#a soma do triplo do primeiro com o terceiro.
b=n1*3+n3
#o terceiro elevado ao cubo.
c=n3**3

print('o produto do dobro do primeiro com metade do segundo é {}'.format(a))
print('a soma do triplo do primeiro com o terceiro é {}'.format(b))
print('o terceiro elevado ao cubo é {:.2f}'.format(c))

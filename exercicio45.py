print('Dados numericos')
res='S'
cont=0
soma=0
menorn=0
maiorn=0
while res in 'S':
    n=int(input('Digite um valor: '))
    cont+=1
    soma=soma+n
    if cont==1:
        maiorn = menorn = n
    else:
        if n>maiorn:
            maiorn=n
        if n<menorn:
            menorn=n
    res=str(input('Quer continuar? [S/N]: ')).upper()
div=soma/cont
print('Você digitou: {} Números \n  A Divisao: {}'.format(cont,div))
print('O maior número é {} \n O menor número é {}'.format(maiorn,menorn))


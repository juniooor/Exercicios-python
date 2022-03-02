#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
print('-----DESAFIO 101-----')
def soma3(a,b,c):
    soma=a+b+c
    return soma

n1=int(input('valor 1: '))
n2=int(input('Valor 2: '))
n3=int(input('valor 3: '))

print(soma3(n1,n2,n3))
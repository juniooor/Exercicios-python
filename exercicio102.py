#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
print('-----DESAFIO 102-----')
def poun(n):
    if n<0:
        return 'O argumento é negativo'
    else:
        return 'Argumento é positivo'

    
x=int(input('Digite um número negativo ou positivo: '))
print(poun(x))
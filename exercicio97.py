#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.

from unicodedata import digit


def leiaint(var):
    while True:
        n=str(input(var))
        if n.isdigit():
            return n 
        else:
            print('ERRO DIGITE UM NUMERO INTEIRO')
n=leiaint('é numero?: ')
print(f'Você digitou {n}')
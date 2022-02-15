#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
print('CHECAR SE A FRASE É UM PALINDROMO')
frase=str(input('Digite uma frase: ')).lower().strip()
palavra=frase.split()
junto=''.join(palavra)
inverso=''
for letra in range(len(junto)-1, -1, -1):
    inverso+=junto[letra]
if inverso == junto:
    print(' É UM PALIDROMO')
else:
    print('NÃO É UM PALIDROMO')


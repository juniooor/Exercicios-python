 #Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras=('SOPA','BATATAS','CACAU','CASTANHA','LASANHA','GOSTOSURAS','TRAVESSURAS','PARMEGIANA')
for p in palavras:
    print(f'\n As Vogais de {p} são: ',end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
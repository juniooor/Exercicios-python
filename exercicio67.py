'''Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma=somac=mlinha=0
for c in range(0,3):
    for l in range(0,3):
        matriz[c][l]=int(input(f'Digite o valor para {c},{l}: '))
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c][l]:^4}]',end='')
        if matriz[c][l]%2==0:
            soma+=matriz[c][l]
    print()
for l in range(0,3):
    somac+= matriz[l][2]

print('---'*20)
print(f'a soma foi {soma}')
print(f'A soma das colunas foi {somac}')
print(f'o maior numero da segunda linha é {max(matriz[1])}')
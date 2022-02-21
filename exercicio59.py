#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 
valor=[]
while True:
    v=int(input('Digite um valor: '))
    if v not in valor:
        valor.append(v)
        print('Valor adcionado!!')
    else:
        print('Valor duplicado!')
    p=str(input('Quer continuar? [S/N]')).upper()
    if p in 'N':
        break
    valor.sort()
print(f'Você digitou os numeros {valor}')
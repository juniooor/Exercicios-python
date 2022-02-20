'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

produtos=('Biscoito',1.90,'Bolacha integral',3.50,'500g Presunto',13.50,'Queijo Mussarella',21.70,'pão',8.30,'Carne moída',18.50,'Manteiga',5.50)
print('--'*20)
print('{:^40}'.format('NOTA FISCAL'))
print('--'*20)
for pos in range(0,len(produtos)):
    if pos%2==0:
        print(f'{produtos[pos]:.<30}', end='.')
    else:
        print(f'R${produtos[pos]:>5.2f}')
print('--'*20)
print('{:^40}'.format('VOLTE SEMPRE!!'))
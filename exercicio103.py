#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
print('-----DESAFIO 103-----')
def somaimposto(taxa,prod):
    taxa=taxa/100
    juros=prod*taxa
    soma=juros+prod
    return soma


produto=float(input('Digite o valor do produto: '))
taxa=float(input('Digite o valor do imposto [%]: '))
result=somaimposto(taxa,produto)

print(f'O produto com imposto fica R${result}')
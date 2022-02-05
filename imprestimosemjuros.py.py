print('Calcule qual a parcela do seu imprestimo bancario sem juros')
s = float(input('Qual o seu salário?: '))
i = float(input('Qual o valor do imprestimo?: '))
p = float(input('Em quantos anos você quer pagar?: '))
m= p *12
p = i/m
t= s*0.3
if p>t:
    print('Imprestimo negado, sua renda é incompátivel com as parcelas')
else:
    print('Emprestimo aprovado com sucesso!! ')

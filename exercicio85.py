#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados={}
dados['nome']=str(input('Nome: '))
ano=int(input('Ano de nascimento: '))
idade= date.today().year-ano
dados['idade']=idade
clt=int(input('Carteira de trabalho: ["0"tem] '))
if clt !=0:
    dados['CLT']=clt
    dados['contratação']=int(input('Ano de contratação: '))
    dados['salario']=float(input('sálario: '))
    tempo_clt= dados['contratação']+35
    anos_aposentar= tempo_clt-date.today().year
    aposentar=anos_aposentar+idade
    dados['aposentar']=aposentar
else:
    dados['CLT']= "Não tem"
for k,v in dados.items():
    print(f'- O {k} tem valor: {v}')
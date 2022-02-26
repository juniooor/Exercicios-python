#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
dados={}
dados['nome']=input('qual é o seu nome?: ')
dados['media']=int(input(f'{dados["nome"]},Qual é a sua media?: '))
if dados['media']>=7:
    dados['resultado']='APROVADO'
else:
    dados['resultado']='REPROVADO'
print(f'{dados["nome"]},sua média foi {dados["media"]}. você está {dados["resultado"]}')
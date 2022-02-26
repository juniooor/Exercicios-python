'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''
#colocar as perguntas em uma lista
perguntas=['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vitima?','Devia para a vitima?','Já trabalhou com a vitima?']
#usar laço para mostrar cada elemento da lista
resposta=[]
for i in perguntas:
    user=str(input(f'{i}:[S/N]')).upper()
    if user in 'Ss': #aqui testo se o usuario digitou 'sim' ele adciona a uma lista de respostas
        resposta.append(user)
resultado=len(resposta) #uso o len para contar quantos 'sim' tem na lista
if resultado==2:
    print('A testemunha é considerada Suspeita!')
elif resultado==5:
    print('A testemunha é o assasino')
    print('DISQUE 1-9-0 !!')
elif resultado==3 or resultado==4:
    print('A testemunha é considerada Cúmplice')
else:
    print('A testemunha é inocente, Está liberada!')

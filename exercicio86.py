#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
dados={}
partidas=[]
dados['nome']=str(input('Qual o nome do jogador?: '))
part=int(input(f'Quantas partidas {dados["nome"]} jogou?: '))
for c in range(0,part):
    partidas.append(int(input(f'Quantos gols fez na {c+1}º partida?: ')))
dados['gols']=partidas
dados['total']=sum(partidas)
print('=-'*25)
print(dados)
print('=-'*25)
for k,v in dados.items():
    print(f'O {k} tem valor {v}')
print('=-'*25)
print(f'O jogador {dados["nome"]} jogou {part} Partidas')
for i,k in enumerate(partidas):
    print(f'Na {i+1}º Partida: {k} Gols')
print(f'Total de {dados["total"]} gols')

    

#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
time=[]
jogador={}
partidas=[]
while True:
    jogador.clear()
    partidas.clear()
    jogador['nome']=str(input('Nome: '))
    part=int(input(f'Quantas partidas {jogador["nome"]} Jogou?: '))
    for p in range(0,part):
        partidas.append(int(input(f'quantos gols na partida {p+1}: ')))
    jogador['gols']=partidas
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        r=str(input('Você deseja continuar?: [S/N]')).upper()
        if r in 'SN':
            break
        print('DIGITE APENAS [S] OU [N]!')
    if r =='N':
        break
print('_'*30)
print('cod ',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for k,v in enumerate(time):
    print(f'{k:>3}',end=' ')
    for c in v.values():
        print(f'{str(c):<15}',end='')
    print()
print('_'*30)
while True:
    busca=int(input('Mostrar os dados de qual jogador? [999 para]: '))
    if busca == 999:
        break
    elif busca>=len(time):
        print(f'Erro!. Não existe jogador com o código {busca}.')
    else:
        print(f'  LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}!!')
        for i, k in enumerate(time[busca]["gols"]):
            print(f' no jogo {i+1} fez {k} gols.!')
print('OBRIGADO E VOLTE LOGO')
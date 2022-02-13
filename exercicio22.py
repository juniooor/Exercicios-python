n1=float(input('Digite sua nota 1: '))
n2=float(input('Digite sua nota 2: '))
n3=float(input('Digite sua nota 3: '))
n4=float(input('Digite sua nota 4: '))
media= (n1+n2+n3+n4)/4

if media>5:
    print('você está de recuperação,tirou {} . estude mais'.format(media))
elif media>=7:
    print('você está aprovado, tirou {}.boas ferias'.format(media))
else:
    print('Você está reprovado tirou {}'.format(media))

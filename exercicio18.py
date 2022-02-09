#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

print('Tempo para download de arquivos')
mb=float(input('QUal o tamanho do arquivo em MB?: '))
net=float(input('Qual a velocidade da internet em mbps?: '))
ts=mb/(net/8)
tm=ts/60
print('O seu arquivo vai baixar em {:.2f} minutos'.format(tm))
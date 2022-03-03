#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

def fusoh(h,m):
    if h == 0:
        fuso='AM'
        h=+12
        return f'{h}:{m} {fuso}'
    elif 1<=h<=11:
        fuso='AM'
        return f'{h}:{m} {fuso}'
    elif 13<=h<=23:
        fuso='PM'
        h=h-12
        return f'{h}:{m} {fuso}'
    else:
        fuso='PM'
        return f'{h}:{m} {fuso}'
    


while True:
    horas=int(input('Digite as horas: '))
    minutos=int(input('digite os minutos: '))
    print('AM:(antes do meio-dia) PM:(depois do meio-dia).')
    print(fusoh(horas,minutos))
    pert=str(input('Deseja continuar?: [S/N]')).upper()
    if pert =='N':
        print('PROGRAMA FINALIZANDO')
        break


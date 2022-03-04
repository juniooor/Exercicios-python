#Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.


from time import sleep
print('-----DESAFIO 105----')

def ValorPagamento(parcela,atraso=0):
    taxa=(atraso*0.001)+atraso
    if atraso !=0:
        atual=parcela+taxa+0.03
        return atual
    else:
        atual=parcela
        return atual


relatorio=[]
while True:
    print('Digite [0] para finalizar e exibir o relatório')
    parc=float(input('Qual o valor da parcela?: '))
    if parc==0:
        break
    perg=str(input('A parcela está em atraso? [S/N]'))
    if perg in 'S':
        atr=int(input('Dias em atraso: '))
        x=ValorPagamento(parc,atr)
        relatorio.append(x)
    else:
        atr=0
        x=ValorPagamento(parc,atr)
        relatorio.append(x)
    print(f'o valor a ser pago é R${x:.2f}')
print(f'foram feitos {len(relatorio)} pagamentos hoje, irei listar cada um dos pagamentos')
print('listando...')
sleep(2)
for i in relatorio:
    print(f'R${i:.2f}',end=' ')


        


            


n=s=cont=0
print('CALCULADORA DE SOMA')
while True:
    n=int(input('Digite um número: [DIGITE 999 PARA PARAR] '))
    if n==999:
        break
    cont+=1
    s+=n
print(f'você digitou {cont} números, a Soma desses números é {s}')
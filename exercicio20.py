print('Digite dois numeros e lhe mostrarei o maior valor')
num1=int(input('Digite o primeiro numero: '))
num2=int(input('Digite o segundo numero: '))
if num1>num2:
    print(' o numero {} é maior que o numero {}'.format(num1,num2))
elif num2>num1:
    print(' o numero {} é maior que o numero {}'.format(num2,num1))
else:
    print('os dois numeros são iguais!')
    
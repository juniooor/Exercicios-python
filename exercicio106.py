#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.


print('-----DESAFIO 106-----')
def lendigit(num):
    srt=str(num)
    return len(srt)


num=int(input('Digite um numero inteiro: '))
x=lendigit(num)
print(f'Você digitou {x} números')
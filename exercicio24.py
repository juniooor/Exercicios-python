# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de #Massa    Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida


print('Calculo de IMC')
kg=float(input('Digite quantos quilos você pesa: '))
h=float(input('Digite sua Altura: '))
imc=kg/(h*2)
if imc<18.5:
    print('Você está abaixo do peso.seu IMC é {}'.format(imc))
elif imc<=25:
    print('Você está no peso ideal. Seu IMC {}'.format(imc))
elif imc<=30:
    print('Você está com sobrePeso. Seu IMC {}'.format(imc))
elif imc<=40:
    print('Você está com obseidade. Seu IMC {}'.format(imc))
else:
    print('Você está com Obesidade Mórbita. Seu IMC {}'.format(imc))
#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7



print('calculo de peso ideal 2')
h=float(input('Digite sua altura: '))
sexo=int(input('digite seu sexo 1 para masculino e 2 para feminino: '))
if sexo == 1 :
    r=72.7*h-58
    print('Seu peso ideal é {:.2f}'.format(r))
else:
    r=62.1*h-44.7
    print('seu peso ideal é {:.2f}'.format(r))    
    



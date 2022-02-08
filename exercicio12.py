#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

print('Calculo do imc')
h=float(input('Digite a sua altura: '))
r=72.7*h -58
print('O seu peso ideal é {}'.format(r))
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.

print('calculo de salario com taxas')
sh=int(input('Digite quanto ganha por hora: '))
ht=int(input('Digite quantas horas trabalha por mes: '))
sb= sh*ht
inss=sb*0.08
sin=sb*0.05
ir=sb*0.11
sl=sb-inss-sin-ir
print('salário bruto: R${}'.format(sb))
print('IR (11%): R${}'.format(ir))
print('INSS (8%): R${}'.format(inss))
print('Sindicato (5%): R${}'.format(sin))
print('Salário liquido: R${}'.format(sl))


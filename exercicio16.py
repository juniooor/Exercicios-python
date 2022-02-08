#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



print('quantos litros precisa para pintar uma parede')
mt=float(input('quantos metros quadrados vão ser pintados?: '))
ct=3
pl=80
cl=18
litros=mt/ct
latas=int(litros/cl)
if litros%cl != 0:
    latas+= 1
    total= latas*pl
    print('você vai precisar de {:.2f} latas e fica um total de R${:.2f}'.format(latas,total)) 

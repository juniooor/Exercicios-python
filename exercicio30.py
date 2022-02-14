#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
total=0
ale=0
for num in range(1,501, 2):
   if num%3==0:
       total+=num
       ale+=1
print(' A soma de todos os {} numeros é {}'.format(ale,total))
        



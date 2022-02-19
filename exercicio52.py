''' Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
#n=int(input('digite um número de 0 a 20: '))
from operator import truediv


num=('Zero','Um','Dois','três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    n=int(input('Digite um número: '))
    if 0<= n <=20:
        break
    print('Tente novamente. ',end='')
print(f'você digitou {num[n]}')
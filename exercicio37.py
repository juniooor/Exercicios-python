#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

sumage=0
nameold=''
oldagemen=0
youngirl=0
for c in range(1,5):
    print('-'*7,'{}º PESSOA'.format(c))
    name=str(input('Digite o nome da {}º pessoa: '.format(c)))
    age=int(input('Digite a idade da {}º pessoa: '.format(c)))
    sex=str(input('Digite o sexo da {}º pessoa [M] ou [F]: '.format(c))).upper()
    sumage+=age
    if c ==1 and sex=='M':
        oldagemen=age
        nameold = name
    if sex=='M' and age>oldagemen:
        oldagemen=age
        nameold=name
        print('O homem mais velho é {}, e ele tem {} anos'.format(nameold,oldagemen))  
    
    else:
        print('não tem homens no grupo')
    if sex=='F':
        if age<20:
            youngirl+=1
average=sumage/4
print('A média da idade das pessoas é {}'.format(average))
print('Tem {} mulher(es) menores de 20 anos'.format(youngirl))
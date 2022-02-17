#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
s=str(input('qual o seu sexo?: ')).upper()
while s not in 'FM':
    s=str(input('dados invalidos digite novamente[M/F]?: ')).upper()
    
print('Obrigado pela resposta!')
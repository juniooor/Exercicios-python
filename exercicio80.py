#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos
idade=[]
altura=[]
for n in range(0,5):
    age=int(input(f'Digite a idade da {n+1}º pessoa: '))
    height=float(input(f'Digite a altura da {n+1}º pessoa: '))
    idade.append(age)
    altura.append(height)
media=sum(altura)/len(altura)
quantaluno=0
for c in range(0,len(idade)):
    if idade[c]>13 and altura[c]<media:
        quantaluno+=1

print(quantaluno)

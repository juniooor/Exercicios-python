'''teste=[]
teste.append('junior')
teste.append('21')
galera=[]
galera.append(teste[:])
teste[0]='leticya'
teste[1]=22
galera.append(teste[:])
print(galera)'''

'''galera=[['junior',21],['leticya',22],['vini',22,'masculino'],['dani',19,'feminino']]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''
maior=menor=0
galera=[]
dado=[]
agem=[]
agef=[]
while True:
    dado.append(str(input('Qual o nome?: ')))
    dado.append(float(input('QUal o peso?: ')))
   # dado.append(str(input('Qual o sexo?: [M/F]').upper()))
    galera.append(dado[:])
    dado.clear()
    r=str(input('Quer continuar?'))
    if r in 'n':
       break 
for p in galera:
    if p[1]>=85:
        agem.append(p[0])
        maior+=1
    elif p[1]<=50:
        agef.append(p[0])
        menor+=1
print(f'temos {maior} maiores de idade e {menor} menores de idade')
print(agem)
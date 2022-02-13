from datetime import date, datetime
ano= date.today().year
birth= int(input('Digite o ano de nascimento do atleta: '))
idade=ano-birth
print('O atleta tem {}'.format(idade))
if idade<=9:
    print('Classificação Mirim.')
elif idade<=14:
    print('Classificação Infantil')
elif idade<=19:
   print('Classificação Junior')
elif idade <=25:
    print('Classificação Sênior')
else:
    print('Classificação Master')
        
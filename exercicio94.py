#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.




def voto(nasc):
    from datetime import date
    atual=date.today().year
    ano=atual-nasc
    if ano<16:
        return f'idade {ano}: NÃO VOTA'
    elif 16<=ano<18 or ano>65:
        return f'idade {ano}: VOTO OPCIONAL'
    else:
        return f'idade {ano}:VOTO OBRIGATÓRIO'



nasc=(int(input('ano: ')))
print(voto(nasc))
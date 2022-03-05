#: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.  

import exercicio109MOD

num=int(input('numero: '))
aut=int(input('Vai aumentar quantos % ?: '))
mid=int(input('Vai diminuir quantos % ?:'))
a=exercicio109MOD.aumentar(num,aut)
d=exercicio109MOD.diminuir(num,mid)
x=exercicio109MOD.metade(num)
z=exercicio109MOD.dobro(num)
print('=-'*20)
print(f'o aumento de {num} em {aut}% é de {a}')
print(f'A redução de {num} em {mid}% é de {d}')
print(f'O dobro de {num} é de {z}')
print(f'A metade de {num} é de {x}')


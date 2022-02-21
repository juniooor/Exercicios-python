# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
exp=str(input('Digite uma expressão: '))
lista=[]
for simblo in exp:
    if simblo == '(':
        lista.append('(')
    elif simblo == ')':
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista)==0:
    print('Sua expressão está válida')
else:
    print('Sua lista está inválida')

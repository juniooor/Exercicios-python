'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)'''
def notas(*n,sit=False):
    r={}
    r['MAIOR']=max(n)
    r['TOTAL']=len(n)
    r['MENOR']=min(n)
    r['MÉDIA']=sum(n)/len(n)
    if sit:
        if r['MÉDIA']>=7:
            r['situação']='BOA'
        elif r['MÉDIA']>=5:
            r['situação']='RAZOAVEL'
        else:
            r['situação']='PESSIMA'
    return r


resp=notas(5.5,4,3,5,sit=True)
print(resp)